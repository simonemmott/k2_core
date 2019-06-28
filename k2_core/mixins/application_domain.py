import k2_util

class ApplicationDomainMixin(object):
    
    def __str__(self):
        return self.domain.title

