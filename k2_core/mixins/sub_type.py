import k2_util

class SubTypeMixin(object):
    
    def __str__(self):
        return self.label
    
    def type_name(self):
        return self.name.upper()

    def type_value(self):
        return self.value.upper()
    
