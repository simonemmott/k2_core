import k2_util

class SubTypeMixin(object):
    
    def __init__(self):
        self.__class__.__str__ = SubTypeMixin.__str__

    def __str__(self):
        return '{model}::{field}[{type}]'.format(
            model=self.field.model.name,
            field=self.field.name,
            type=self.type_name()
        )
    
    def type_name(self):
        return self.name.upper()

    def type_value(self):
        return self.value.upper()
    
