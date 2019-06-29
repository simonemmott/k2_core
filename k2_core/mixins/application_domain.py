from . import register

class ApplicationDomainMixin(object):
    
    @register('k2_app.models.application_domain', 'ApplicationDomain')
    def __str__(self):
        return self.domain.title

