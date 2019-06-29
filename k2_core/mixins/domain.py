from . import register

class DomainMixin(object):
    
    @register('k2_domain.models.domain', 'Domain')
    def __str__(self):
        return self.title