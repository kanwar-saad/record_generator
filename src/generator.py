import sys, random, string
import simplejson as json
from ordereddict import OrderedDict
from pprint import pprint
import globals


# Abstract Base Class for Fields
class Field(object):
    def __init__(self, *args, **kwargs):

        val_list = kwargs.get('val_list')
        val_range = kwargs.get('val_range')
        if (val_list and val_range):
            print "Cannot specify both value range and value list in field", name
            raise BaseException()
        #print "name =", kwargs['name']
        self.name = kwargs['name']
        self.val_list = val_list
        self.val_range = val_range

    def __str__(self):
        raise NotImplementedError( "__str__ function not implemented" )
    def generate_val(self):
        raise NotImplementedError( "generate_val function not implemented" )



class CharField(Field):
    def __init__(self, size, *args, **kwds):
        Field.__init__(self, *args, **kwds)
        self.size = size
        if size == 0:
            print "Warning: Generating Char[n] with n = 0"

    def random_str_generator(self, size=6, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
        return ''.join(random.choice(chars) for x in range(size))

    def generate_val(self):
        self.value = None

        if self.val_list:
            self.value = random.choice(self.val_list)
        else:
            self.value = self.random_str_generator(self.size)
        


    def __str__(self):
        if (not self.value):
            return "<None>"
        else:
            return self.value

class Uint8Field(Field):
    def __init__(self, *args, **kwds):
        Field.__init__(self, *args, **kwds)
        if (not self.val_list) and (not self.val_range):
            print "No values specified for field", self.name
            raise BaseException()


    def generate_val(self):
        self.value = None
        if self.val_list:
            # Assuming value list are all int
            self.value = random.choice(self.val_list)
        elif self.val_range:
            # assuming ranges are given in int
            self.value = random.randint(self.val_range[0], self.val_range[1])

        if self.value == None:
            print "Warning: No Field Generated in "+self.name

    def __str__(self):
        if not self.value:
            return "<None>"
        else:
            return str(self.value)

def get_field_object(field):
    type = field['type']
    ret = None

    if type == "BCD":
        pass
    elif type == "BCD8":
        pass
    elif type == "BIN":
        pass
    elif type == "CHAR":
        ret = CharField(size=field['size'], name=field.get('name'), val_list=field.get('values'))
    
    elif type == "BCDTIMESTAMP":
        pass
    elif type == "IPADDR":
        pass
    elif type == "TIME64":
        pass
    elif type == "UINT8":
        ret = Uint8Field(name=field.get('name'), val_list=field.get('values'), val_range=field.get('value_range'))
    elif type == "UINT16":
        pass
    elif type == "UINT32":
        pass
    elif type == "UINT64":
        pass

    
    return ret
def generator_init():

    for schema, value in globals.edg_schema.items()[:]:
        globals.edg_gen_fields[schema] = []
        for field, prop in value['fields'].items():
            #print "processing field :", field
            prop['name'] = field
            field_obj = get_field_object(prop)
            if not field_obj:
                print "get_field_object returned null for schema="+schema+", field="+field
                return False
            globals.edg_gen_fields[schema].append(field_obj)

    return True
def generate_record(schema):
    ret = []
    for gen_obj in globals.edg_gen_fields[schema]:
        
        gen_obj.generate_val()
        ret.append(gen_obj)
    return ret
