import k2_util

class MemberMixin(object):
    
    def __str__(self):
        return '{type}: {cls}::{field}({title})'.format(
            type=self.get_type_display(),
            cls=self.model.class_name(),
            field=self.name,
            title=self.title
        )

