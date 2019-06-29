import k2_util
from . import register

class SubTypeMixin(object):
    
    @register('k2_domain.models.sub_type', 'SubType')
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
    
