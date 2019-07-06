from . import register

class MemberMixin(object):
    
    @register('k2_domain.models.member', 'Member')
    def __str__(self):
        return '{type}::{field}({title})'.format(
            type=self.base_type.name,
            field=self.name,
            title=self.title
        )

