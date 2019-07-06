import k2_util

class FieldMixin(object):
    
    def __init__(self):
        if not hasattr(self.__class__, '_related_types'):
            setattr(self.__class__, '_related_types', [self.__class__.FieldType.LINKED])

        if not hasattr(self.__class__, '_on_delete_names'):
            setattr(self.__class__, '_on_delete_names', {
                self.__class__.OnDeleteType.CASCADE: 'CASCADE',
                self.__class__.OnDeleteType.PROTECT: 'PROTECT',
                self.__class__.OnDeleteType.SET_NULL: 'SET_NULL'
            })

    
    def types_name(self):

        return '{name}Type'.format(name=k2_util.to_class_case(self.name))
    
    def field_class_name(self):
        if self.field_type == self.__class__.FieldType.BOOLEAN:
            return 'BooleanField'
        if self.field_type == self.__class__.FieldType.NULL_BOOLEAN:
            return 'NullBooleanField'
        if self.field_type == self.__class__.FieldType.STRING:
            return 'CharField'
        if self.field_type == self.__class__.FieldType.DATE:
            return 'DateField'
        if self.field_type == self.__class__.FieldType.DATE_TIME:
            return 'DateTimeField'
        if self.field_type == self.__class__.FieldType.DECIMAL:
            return 'DecimalField'
        if self.field_type == self.__class__.FieldType.EMAIL:
            return 'EmailField'
        if self.field_type == self.__class__.FieldType.FILE:
            return 'FileField'
        if self.field_type == self.__class__.FieldType.IMAGE:
            return 'ImageField'
        if self.field_type == self.__class__.FieldType.INTEGER:
            return 'IntegerField'
        if self.field_type == self.__class__.FieldType.POSITIVE_INTEGER:
            return 'PositiveIntegerField'
        if self.field_type == self.__class__.FieldType.TEXT:
            return 'TextField'
        if self.field_type == self.__class__.FieldType.TIME:
            return 'TimeField'
        if self.field_type == self.__class__.FieldType.URL:
            return 'UrlField'
        if self.field_type == self.__class__.FieldType.LINKED:
            return 'ForeignKey'
        if self.field_type == self.__class__.FieldType.SUB_TYPE:
            return 'CharField'
        
        raise ValueError('No field class defined for field of {type} - ({disp})'.format(type=self.field_type, disp=self.get_field_type_display()))
    
    def title_or_link_type(self):
        if self.field_type in [self.__class__.FieldType.LINKED]:
            if self.data_type.model.domain == self.member_of_type.model.domain:
                return self.data_type.model.class_name()
            return '{domain}.{model}'.format(domain=self.data_type.model.domain.name, model=self.data_type.model.class_name())
        return self.title
    
    def model_field_options(self):
        return  self._on_delete_clause()+\
                self._verbose_name_clause()+\
                self._default_clause()+\
                self._max_length_clause()+\
                self._choices_clause()+\
                self._null_clause()+\
                self._blank_clause()+\
                self._help_text_clause()
                   
    def _on_delete_clause(self):
        if self.field_type in self.__class__._related_types:
            return ', on_delete=models.{v}'.format(v=self.__class__._on_delete_names.get(self.on_delete_type, '__ERR__'))
        return ''
        
                
    def _verbose_name_clause(self):
        if self.field_type in self.__class__._related_types:
            return ', verbose_name="{v}"'.format(v=self.title.replace('"', "'"))
        return ''
    
    def _help_text_clause(self):
        if len(self.description) > 0 and len(self.description) < 100:
            return ', help_text="{v}"'.format(v=self.description.replace('"', "'"))
        return ''
    
    def _max_length_clause(self):
        if self.max_length and self.max_length > 0:
            return ', max_length={v}'.format(v=self.max_length)
        return ''
    
    def _choices_clause(self):
        if self.field_type == self.__class__.FieldType.SUB_TYPE:
            return ', choices={v}.CHOICES'.format(v=self.types_name())
        return ''
    
    def _blank_clause(self):
        if self.required != None and self.required == True:
            return ', blank=False'
        return ', blank=True'
    
    def _null_clause(self):
        return ', null=True'
    
    def _default_clause(self):
        if not self.default_value:
            return ''
        if self.data_type == self.__class__.DataType.BOOLEAN:
            if self.default_value.upper() in ['', '0', 'FALSE', 'NO']:
                return ', default=False'
            return ', default=True'
        if self.data_type in [self.__class__.DataType.INTEGER, self.__class__.DataType.FLOAT]:
            return ', default={v}'.format(v=self.default_value)  
        if self.data_type in [self.__class__.DataType.STRING, self.__class__.DataType.DATE]:
            return ', default="{v}"'.format(v=self.default_value.replace('"', "'"))  
        return ''

    
