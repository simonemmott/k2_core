import k2_util

class ApplicationDomainMixin(object):
    
    def __init__(self):
        self.__class__.__str__ = ApplicationDomainMixin.__str__

    def __str__(self):
        return self.domain.title

