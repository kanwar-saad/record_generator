import sys, json
import globals


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
            globals.edg_schema[key] = json.load(schema_data_json)
        except ValueError as e:
            print "Error parsing JSON in schema file : ", schema_file
            print e
            return False

        #pprint (globals.edg_schema[key])
        print "  "+key+" schema parsed from file " + schema_file
    return True


def validate_schema_structure():
    for schema, schema_data in globals.edg_schema.items():
        if 'name' not in schema_data:
            print schema, "schema does not contain mandatory 'name' tag"
            return False
        if 'fields' not in schema_data:
            print schema, "schema does not contain mandatory 'fields' tag"
            return False

        for field_key, field_meta in globals.edg_schema[schema]['fields'].items():
            if 'type' not in field_meta:
                print "Mandatory 'type' tag missing in", schema,": fields :", field_key
                return False

        print "  "+schema+" schema structure validated"
    return True

def schema_post_process():
    return True

