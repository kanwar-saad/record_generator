import sys, re
import simplejson as json
from ordereddict import OrderedDict
from pprint import pprint
import globals

def print_schema():
    for schema in globals.edg_schema.values():
        pprint (schema['fields'].keys())

def parse_schema_files():
    meta_info = globals.edg_conf['conf']['metadata_info']
    for key, value in meta_info.items():

        schema_file = value['schema_path']
        # Check whether file exist or not
        try:
            with open(schema_file) as f: pass
        except IOError as e:
            print 'Error : Schema file: "%s", do not exist'% schema_file
            return False

        # Parse JSON data in schema file
        schema_data_json = open(schema_file)
        try:
            str_data = bytearray(schema_data_json.read()).decode('utf-8')
            globals.edg_schema[key] = json.loads(str_data, object_pairs_hook=OrderedDict)
            schema_data_json.close()
        except ValueError as e:
            print "Error parsing JSON in schema file : ", schema_file
            print e
            return False

        #pprint (globals.edg_schema[key])
        print "  "+key+" schema parsed from file " + schema_file
    return True


def format_field_type(field):
    field_type = field['type']

    # Match field_type with pre-defined fixed size data_types
    for t in globals.edg_field_types_const:
        if field_type == t:
            return True
    
    # Match field_type with pre-defined variable size data_types
    # If matched then modify type value as defined in globals
    # and add additional 'size' tag in field metadata

    for vt in globals.edg_field_types_var:
        res = re.match(vt+'\((.*)\)$', field_type, 0)
        if res:
            try:
                size = int(res.group(1))
            except:
                continue
            field['type'] = vt
            field['size'] = size
            return True

    # If nothing is matched then invalid field type is specified
    return False

def load_values_from_file(schema, field_key, values):
    new_values = []

    for val in values[:]:   # we need to modify the list in loop so iterate over a copy
        if isinstance(val, basestring):
            if val[0] == '@':
                value_file = val[1:]
                # Check whether file exist or not
                try:
                    with open(value_file) as f: pass
                except IOError as e:
                    print 'Error : Values file: "%s", do not exist'% value_file, " for ", schema, ": fields :", field_key, ": values"
                    return False

                # Parse JSON data in schema file
                values_data_json = open(value_file)
                try:
                    values_data = json.load(values_data_json)
                    values_data_json.close()
                except ValueError as e:
                    print "Error parsing JSON values in values file : ", value_file, " for ", schema, ": fields :", field_key, ": values"
                    print e
                    return False

                # Values data should be in the following format
                # {"values":[val1, val2, val3, ... ]}
                # values datatype should match the type field. This is the responsibility of user.
                # duplications will be removed
                values.extend(values_data.get('values')) 
                values.remove(val)

    #remove duplicates
    values[:] = list(set(values))
    return True

def validate_fields(schema, fields_meta):
    for field_key, field_meta in fields_meta.items():
        if 'type' not in field_meta:
            print "Mandatory 'type' tag missing in", schema,": fields :", field_key
            return False

        if not format_field_type(fields_meta[field_key]):
            print "Invalid field 'type' in", schema,": fields :", field_key
            return False

        # 'values' tag in field metadata contains pre-defined values.
        # if it contains a value with @ then values should be loaded from file whose name
        # is followed by @
        
        if 'values' in fields_meta[field_key]:
            if not load_values_from_file(schema, field_key, fields_meta[field_key]['values']):
                return False

    return True

def validate_schema_structure():

    for schema, schema_data in globals.edg_schema.items():
        if 'name' not in schema_data:
            print schema, "schema does not contain mandatory 'name' tag"
            return False
        if 'fields' not in schema_data:
            print schema, "schema does not contain mandatory 'fields' tag"
            return False
        
        if not validate_fields(schema, globals.edg_schema[schema]['fields']):
            return False

        #for field_key, field_meta in globals.edg_schema[schema]['fields'].items():
        #    if 'type' not in field_meta:
        #        print "Mandatory 'type' tag missing in", schema,": fields :", field_key
        #        return False
        
        print "  "+schema+" schema structure validated"

    return True


def include_schema():
     
    for schema, value in globals.edg_schema.items()[:]:
        schema_data = OrderedDict()
        schema_files = [globals.edg_conf['conf']['metadata_info'][schema]['schema_path']]

        # Continue to next schema if this schema has no other include files
        if not value.get('include_schema'):
            continue
        # Check for self inclusion
        if list(set(schema_files) & set(value.get('include_schema'))):
            print "Error: Cannot self include schema in %s : schema_include"% schema
            return False

        # Check for duplicate inclusion 
        schema_files = value.get('include_schema')
        if len(list(set(schema_files))) != len(schema_files):
            print "Error: File duplication in %s : schema_include list "% schema
            return False

        for schema_file in schema_files:
            # Check whether file exist or not
            try:
                with open(schema_file) as f: pass
            except IOError as e:
                print 'Error : Included schema file: "%s", do not exist'% schema_file
                return False

            # Parse JSON data in schema file
            schema_data_json_file = open(schema_file)
            str_data = bytearray(schema_data_json_file.read()).decode("utf-8")
            schema_data_json = re.sub(r'<Application>', globals.edg_schema[schema]['name'], str_data)
            try:
                schema_data[schema_file] = json.loads(schema_data_json, object_pairs_hook=OrderedDict)
                schema_data_json_file.close()
            except ValueError as e:
                print "Error parsing JSON in included schema file : ", schema_file
                print e
                return False

            print "Include Schema File " + schema_file + " Parsed"

            # Check for more than one level of include
            if schema_data[schema_file].get('include_schema'):
                print "Error: more than one level of schema nesting in", schema, ": include_schema :", schema_file
                return False

            # Schema structure validation and expansion
            if 'name' not in schema_data[schema_file]:
                print schema_file, "schema does not contain mandatory 'name' tag"
                return False
            if 'fields' not in schema_data[schema_file]:
                print schema_file, "schema does not contain mandatory 'fields' tag"
                return False
            
            if not validate_fields(schema_file, schema_data[schema_file]['fields']):
                return False
        
        # Tweak for maintaining order of included fields
        ordered_fields = OrderedDict()
        for schema_file in schema_files:
            key_intersect = list(set(ordered_fields.keys()) & set(schema_data[schema_file]['fields'].keys()))
            if (key_intersect):
                print "Following duplicate keys found in nested schema file: ", schema_file, "in", schema
                print key_intersect
                return False
            
            ordered_fields.update(schema_data[schema_file]['fields'])

        # Now add fields of the Top schema
        key_intersect = list(set(ordered_fields.keys()) & set(value['fields'].keys()))
        if (key_intersect):
            print "Following duplicate keys found in top level schema file of", schema
            print key_intersect
            return False
        
        ordered_fields.update(value['fields'])

        globals.edg_schema[schema]['fields'] = ordered_fields        
        #value['fields'].update(schema_data[schema_file]['fields'])
            






    return True
def schema_post_process():

    # Include nested schemas and validate their fields.
    # - Only one level of include is supported right now.
    # - Multiple includes of same file will throw an error.
    # - Multiple levels of include will throw an error 
    # - For the time being the nested schema files can contain only two significant tags:
    #   1. 'include_schema' : to include additional files
    #   2. 'fields' : To add fields in the parent schema
    #

    if not include_schema():
        return False

    print_schema()
    
    return True






