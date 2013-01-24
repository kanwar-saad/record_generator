import sys, random, string
import simplejson as json
from ordereddict import OrderedDict
from pprint import pprint
import globals



class Output(object):
    def __init__(self, *args, **kwargs):
        self.dst = kwargs['destination']

        if (not self.dst):
            print "Error: No Output destination found"
            raise BaseException()

    def out(self, record=None):
        raise NotImplementedError( "out function not implemented in class: " + self.__name__ )
    def close(self):
        raise NotImplementedError( "close function not implemented in class: " + self.__name__ )

class File(Output):
    def __init__(self, *args, **kwargs):
        Output.__init__(self, *args, **kwargs)
        self.filename = self.dst
        try:
            self.file = open(self.filename, 'w', 0)
            if not self.file:
                print "Error in opening output file :", self.filename
                raise BaseException()

        except:
            print "Error in opening output file :", self.filename 
            raise BaseException()

    def out(self, record=None):
        if not record:
            print "Error: No record passed to format"
            return False

        self.file.write(record)
        self.file.write('\n')
        return True

    def close(self):
        self.file.close()


def output_init():
    type = globals.edg_conf['conf']['output_type']
    if (type == 'file'):
        globals.edg_output = File(destination=globals.edg_conf['conf']['output_destination'])
    else:
        print "Unknown Output Type"
        return False

    return True

def record_out(record):
    ret = None
    if not record:
        print "No record specified for formatting"
        return None

    return globals.edg_output.out(record)


