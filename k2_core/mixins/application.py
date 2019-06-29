from . import register

class ApplicationMixin(object):
    
    @register('k2_app.models.application', 'Application')
    def __str__(self):
        return self.title

