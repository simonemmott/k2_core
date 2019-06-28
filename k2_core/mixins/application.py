import k2_util

class ApplicationMixin(object):
    
    def __init__(self):
        self.__class__.__str__ = ApplicationMixin.__str__

    def __str__(self):
        return self.title

