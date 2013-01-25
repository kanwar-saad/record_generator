import sys
import simplejson as json
from pprint import pprint
import globals
from schema import *
from schedular import *
from generator import *
from format import *
from output import *

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
    
    print 
    print

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

    if not schema_post_process():
        print "Error in Post Processing Schema ... Exiting"
        return

    
    # Initialize schedular
    if not schedular_init():
        print "Error in Initializing Schedular ... Exiting"
        return

    # Initialize generator
    if not generator_init():
        print "Error in Initializing Generator ... Exiting"
        return
    # Initialize formattor
    if not format_init():
        print "Error in Initializing Formatter ... Exiting"
        return

    # Initialize output
    if not output_init():
        print "Error in Initializing Output ... Exiting"
        return



    print "Initialization Complete"
    # Start generator loop.
    count = 0
    while (True):
        sched = get_next_schedule()

        #print sched['schema'], sched['timestamp']
        # Check for termination condition
        if (sched['schema'] == ''):
            break
        count += 1

        # Generate Record
        raw_record = generate_record(sched['schema'])
        raw_record.insert(0, sched['timestamp'])
        raw_record.insert(1, sched['schema'])
        # Output Record
        formatted_record = format_record(raw_record)
        #print formatted_record
        
        if not record_out(formatted_record):
            print "Error in record output ... exiting"
            print "Total records generated = ", count 
            return

    print "Total records generated = ", count 
     
    globals.edg_output.close()





if __name__ == "__main__":
    main(sys.argv[1:])
