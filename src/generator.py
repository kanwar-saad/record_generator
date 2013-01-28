import sys, random, string, datetime
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
            str = self.value.replace('"','\\"')
            ret = "\""
            ret += str
            ret += "\""
 
            return ret

class Uint8Field(Field):
    def __init__(self, *args, **kwds):
        Field.__init__(self, *args, **kwds)

    def generate_val(self):
        self.value = None
        if self.val_list:
            # Assuming value list are all int
            self.value = random.choice(self.val_list)
        elif self.val_range:
            # assuming ranges are given in int
            self.value = random.randint(self.val_range[0], self.val_range[1])
        else:
            self.value = random.randint(0, 255)

        if self.value == None:
            print "Warning: No Field Generated in "+self.name

    def __str__(self):
        if not self.value:
            return "<None>"
        else:
            return str(self.value)


class Uint16Field(Field):
    def __init__(self, *args, **kwds):
        Field.__init__(self, *args, **kwds)

    def generate_val(self):
        self.value = None
        if self.val_list:
            # Assuming value list are all int
            self.value = random.choice(self.val_list)
        elif self.val_range:
            # assuming ranges are given in int
            self.value = random.randint(self.val_range[0], self.val_range[1])
        else:
            self.value = random.randint(0, 65535)

        if self.value == None:
            print "Warning: No Field Generated in "+self.name

    def __str__(self):
        if not self.value:
            return "<None>"
        else:
            return str(self.value)

class Uint32Field(Field):
    def __init__(self, *args, **kwds):
        Field.__init__(self, *args, **kwds)

    def generate_val(self):
        self.value = None
        if self.val_list:
            # Assuming value list are all int
            self.value = random.choice(self.val_list)
        elif self.val_range:
            # assuming ranges are given in int
            self.value = random.randint(self.val_range[0], self.val_range[1])
        else:
            self.value = random.randint(0, 4294967296)

        if self.value == None:
            print "Warning: No Field Generated in "+self.name

    def __str__(self):
        if not self.value:
            return "<None>"
        else:
            return str(self.value)

class Uint64Field(Field):
    def __init__(self, *args, **kwds):
        Field.__init__(self, *args, **kwds)

    def generate_val(self):
        self.value = None
        if self.val_list:
            # Assuming value list are all int
            self.value = random.choice(self.val_list)
        elif self.val_range:
            # assuming ranges are given in int
            self.value = random.randint(self.val_range[0], self.val_range[1])
        else:
            self.value = random.randint(0, 18446744073709552000)

        if self.value == None:
            print "Warning: No Field Generated in "+self.name

    def __str__(self):
        if not self.value:
            return "<None>"
        else:
            return str(self.value)

class BCDField(Field):
    def __init__(self, size, *args, **kwds):
        Field.__init__(self, *args, **kwds)
        self.size = size
    def generate_val(self):
        self.value = None
        if self.val_list:
            # Assuming value list are all int
            self.value = random.choice(self.val_list)
        elif self.val_range:
            # assuming ranges are given in int
            self.value = random.randint(self.val_range[0], self.val_range[1])
        else:
            self.value = int(''.join(random.choice(string.digits) for x in range(self.size)))

        if self.value == None:
            print "Warning: No Field Generated in "+self.name

    def __str__(self):
        if not self.value:
            return "<None>"
        else:
            return str(self.value)


class BCD8Field(Field):
    def __init__(self, size, *args, **kwds):
        Field.__init__(self, *args, **kwds)
        self.size = size
    def generate_val(self):
        self.value = None
        if self.val_list:
            # Assuming value list are all int
            self.value = random.choice(self.val_list)
        elif self.val_range:
            # assuming ranges are given in int
            self.value = random.randint(self.val_range[0], self.val_range[1])
        else:
            self.value = int(''.join(random.choice(string.digits) for x in range(self.size)))

        if self.value == None:
            print "Warning: No Field Generated in "+self.name

    def __str__(self):
        if not self.value:
            return "<None>"
        else:
            return str(self.value)

class BCDDateTimeField(Field):
    def __init__(self, *args, **kwds):
        Field.__init__(self, *args, **kwds)
    
    def generate_val(self):
        self.value = None
        if self.val_list:
            # Assuming value list are all int
            sel = random.choice(self.val_list)
            try:
                self.value = datetime.datetime.strptime(sel, "%H:%M:%S:%f %d-%m-%Y")
            except:
                print "Incorrect datetime format in field:", self.name
                raise BaseException()
        elif self.val_range:
            try:
                val1 = datetime.datetime.strptime(self.val_range[0], "%H:%M:%S:%f %d-%m-%Y")
                val2 = datetime.datetime.strptime(self.val_range[1], "%H:%M:%S:%f %d-%m-%Y")
            except:
                print "Incorrect datetime format in field:", self.name
                raise BaseException()

            if val1 > val2 :
                print "First date is newer than second date in value_range of field:", self.name
                raise BaseException()

            dt = datetime.datetime(1,1,1)
            if (val1.hour != val2.hour):
                dt = dt.replace(hour=random.randint(val1.hour, val2.hour))
            else:
                dt = dt.replace(hour=val1.hour)

            if (val1.min != val2.min):
                dt = dt.replace(minute=random.randint(val1.minute, val2.minute))
            else:
                print val1.min
                dt = dt.replace(minute=val1.minute)

            if (val1.second != val2.second):
                dt = dt.replace(second=random.randint(val1.second, val2.second))
            else:
                dt = dt.replace(second=val1.second)

            if (val1.microsecond != val2.microsecond):
                dt = dt.replace(microsecond=random.randint(val1.microsecond, val2.microsecond)//10000)
            else:
                dt = dt.replace(microsecond=val1.microsecond)

            if (val1.day != val2.day):
                dt = dt.replace(day=random.randint(val1.day, val2.day))
            else:
                dt = dt.replace(day=val1.day)

            if (val1.month != val2.month):
                dt = dt.replace(month=random.randint(val1.month, val2.month))
            else:
                dt = dt.replace(month=val1.month)

            if (val1.year != val2.year):
                dt = dt.replace(year=random.randint(val1.year, val2.year))
            else:
                dt = dt.replace(year=val1.year)

            self.value = dt
        else:
            dt = datetime.datetime(1,1,1)
            dt = dt.replace(hour=random.randint(0, 23))
            dt = dt.replace(minute=random.randint(0, 59))
            dt = dt.replace(second=random.randint(0, 59))
            dt = dt.replace(microsecond=random.randint(0, 99)//10000)
            dt = dt.replace(day=random.randint(1, 28))
            dt = dt.replace(month=random.randint(1, 12))
            dt = dt.replace(year=random.randint(1900, 2029))
            self.value = dt

        if self.value == None:
            print "Warning: No Field Generated in "+self.name

    def __str__(self):
        if not self.value:
            return "<None>"
        else:

            str = self.value.strftime("%H:%M:%S:%%d %d-%m-%Y")
            str  = str % (self.value.microsecond//10000)
            str = str.replace('"','\\"')

            ret = "\""
            ret += str
            ret += "\""
            return ret

class Time64Field(Field):
    def __init__(self, size, *args, **kwds):
        Field.__init__(self, *args, **kwds)
    
    def generate_val(self):
        self.value = None
        if self.val_list:
            # Assuming value list are all int
            sel = random.choice(self.val_list)
            if isinstance( sel, ( int, long ) ):
                self.value = sel
            else:
                print "Incorrect time tick format in field:", self.name
                raise BaseException()

        elif self.val_range:
            val1 = self.val_range[0]
            val2 = self.val_range[1]
            
            if val1 > val2 :
                print "First tick is newer than second tick in value_range of field:", self.name
                raise BaseException()
            
            if isinstance( val1, ( int, long ) ) and isinstance( val2, ( int, long ) ):
                self.value = random.randint(val1, val2)
            else:
                print "Incorrect time tick format in field:", self.name
                raise BaseException()

        else:
            self.value = random.randint(0, 18446744073709552000)

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
    
    # Variable size fields
    if type == "BCD":
        ret = BCDField(size=field['size'], name=field.get('name'), val_list=field.get('values'), val_range=field.get('value_range'))
    elif type == "BCD8":
        ret = BCD8Field(size=field['size'], name=field.get('name'), val_list=field.get('values'), val_range=field.get('value_range'))
    elif type == "BIN":
        pass
    elif type == "CHAR":
        ret = CharField(size=field['size'], name=field.get('name'), val_list=field.get('values'))
    
    # Fixed Size Fields
    elif type == "BCDTIMESTAMP":
        ret = BCDDateTimeField(name=field.get('name'), val_list=field.get('values'), val_range=field.get('value_range'))
    elif type == "IPADDR":
        pass
    elif type == "TIME64":
        ret = Time64Field(name=field.get('name'), val_list=field.get('values'), val_range=field.get('value_range'))
    elif type == "UINT8":
        ret = Uint8Field(name=field.get('name'), val_list=field.get('values'), val_range=field.get('value_range'))
    elif type == "UINT16":
        ret = Uint16Field(name=field.get('name'), val_list=field.get('values'), val_range=field.get('value_range'))
    elif type == "UINT32":
        ret = Uint32Field(name=field.get('name'), val_list=field.get('values'), val_range=field.get('value_range'))
    elif type == "UINT64":
        ret = Uint64Field(name=field.get('name'), val_list=field.get('values'), val_range=field.get('value_range'))

    
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
