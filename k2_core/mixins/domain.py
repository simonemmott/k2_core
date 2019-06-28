import k2_util

class DomainMixin(object):
    
    def __init__(self):
        self.__class__.__str__ = DomainMixin.__str__

    def __str__(self):
        return self.title