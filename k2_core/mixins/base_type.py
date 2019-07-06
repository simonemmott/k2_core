import k2_util
from k2_domain.models.member import Member
from k2_domain.models.field import Field
from . import register

class BaseTypeMixin(object):
    
    @register('k2_domain.models.base_type', 'BaseType')
    def __str__(self):
        return self.name
    
    def basename(self):
        if '.' in self.name:
            return self.name.split('.')[-1]
        return name
    
    def module_name(self):
        if '.' in self.name:
            return self.name.split('.')[:-1]
        return ''
    
