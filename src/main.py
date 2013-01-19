import sys, json
from pprint import pprint
import globals
from schema import *

def validate_conf_structure():
    conf = globals.edg_conf
    if not conf.get('conf'):
        print "Mandatory 'conf' tag not found in Config file"
        return False

    if 'output_type' not in conf['conf']:
        print "Mandatory 'output_type' tag missing in Conf File"
        return False
    if 'output_destination' not in conf['conf']:
        print "Mandatory 'output_destination' tag missing in Conf File"
        return False
    if 'output_format' not in conf['conf']:
        print "Mandatory 'output_format' tag missing in Conf File"
        return False
    if 'metadata_info' not in conf['conf']:
        print "Mandatory 'metadata_info' tag missing in Conf File"
        return False

    for key, value in conf['conf']['metadata_info'].items():
        if 'output_rate' not in value:
            print "Mandatory 'output_rate' tag missing in conf : metadata_info :", key
            return False
        if 'number_of_records' not in value:
            print "Mandatory 'number_of_records' tag missing in conf : metadata_info :", key
            return False
        if 'schema_path' not in value:
            print "Mandatory 'schema_path' tag missing in conf : metadata_info :", key
            return False

    return True

def usage():
    print "Usage: python main <conf_file>"
    print "  <conf_file>\tThe Configuration file that contains the required information for record generation."

def main(argv=None):
    if not argv or (len(argv)>1):
        usage()
        return

    # Check if the conf file exist or not
    conf_file = argv[0]
    try:
        with open(conf_file) as f: pass
    except IOError as e:
        print 'Error : Configuration file: "%s", do not exist'% conf_file
        return

    # Parse JSON data in conf file
    conf_data_json = open(conf_file)
    try:
        globals.edg_conf = json.load(conf_data_json)
    except ValueError as e:
        print "Error in parsing conf file : ", conf_file
        print e
        return

    #pprint(globals.edg_conf)
    conf_data_json.close()

    # Validate conf file structure.
    if not validate_conf_structure():
        print "Error validating conf file ... Exiting"
        return

    print "Config file parsed from file : "+conf_file

    # Parse each schema file mentioned in metadata_info conf 
    print "Start parsing schema files : "
    if not parse_schema_files():
        print "Error parsing schema files ... Exiting"
        return
    # Check for mandatory tags in schema files
    print "Start validating schema files : "
    if not validate_schema_structure():
        print "Error validating schema files ... Exiting"
        return


if __name__ == "__main__":
    main(sys.argv[1:])
