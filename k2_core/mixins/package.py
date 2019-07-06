import k2_util
from . import register

class PackageMixin(object):
    
    @register('k2_app.models.package', 'Package')
    def __str__(self):
        return self.name
    

