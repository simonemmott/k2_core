from . import register

class MemberMixin(object):
    
    @register('k2_app.models.member', 'Member')
    def __str__(self):
        return '{type}::{field}({title})'.format(
            type=self.member_of_type.name,
            field=self.name,
            title=self.title
        )

