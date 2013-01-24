import sys, random, string
import simplejson as json
from ordereddict import OrderedDict
from pprint import pprint
import globals



class Format(object):
    def __init__(self, *args, **kwargs):
        pass
    def format(self, record=None):
        raise NotImplementedError( "out function not implemented in class: " + self.__name__ )


class CSV(Format):
    def __init__(self, delimeter=',', *args, **kwargs):
        Format.__init__(self, *args, **kwargs)
        self.delimeter = delimeter

    def format(self, record=None):
        ret = ''
        if not record:
            print "Error: No record passed to format"
            return ret

        for item in record:
           ret += item.__str__()
           ret += self.delimeter

        return ret

def format_init():
    format = globals.edg_conf['conf']['output_format']
    if (format == 'CSV'):
        globals.edg_formatter = CSV()
    else:
        print "Unknown Output Format"
        return False

    return True

def format_record(record):
    ret = None
    if not record:
        print "No record specified for formatting"
        return None

    return globals.edg_formatter.format(record)

