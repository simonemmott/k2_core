from . import register
import k2_util

class DomainMixin(object):
    
    @register('k2_domain.models.domain', 'Domain')
    def __str__(self):
        return self.title
    
    def config_class_name(self):
        return '{name}Config'.format(name=k2_util.to_class_case(self.title))
    
    