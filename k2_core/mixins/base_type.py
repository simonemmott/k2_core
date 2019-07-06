import k2_util

from . import register

class BaseTypeMixin(object):
    
    @register('k2_app.models.base_type', 'BaseType')
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
    
