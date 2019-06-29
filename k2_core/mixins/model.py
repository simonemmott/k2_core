import k2_util
from k2_domain.models.member import Member
from k2_domain.models.field import Field
from . import register

class ModelMixin(object):
    
    def fields(self):
        return self.members.filter(type=Member.Type.FIELD)
    
    def type_fields(self):
        types = []
        for member in self.fields():
            if member.field.field_type == Field.FieldType.SUB_TYPE:
                types.append(member.field)
        return types
    
    @register('k2_domain.models.model', 'Model')
    def __str__(self):
        return self.title
    
    def class_name(self):
        return k2_util.to_class_case(self.name)
    
    def package_name(self):
        return k2_util.to_snake_case(self.name)
    
    def fields(self):
        return Field.objects.filter(model=self)
    
    def plural_title(self):
        return self.p_title if self.p_title else k2_util.to_plural(self.title)
    
