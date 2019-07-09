from rest_framework import serializers
from k2_util import strip_dict, filter_dict

class RelatedModelSerializer(serializers.ModelSerializer):
    
    def __init__(self, *args, **kw):
        super().__init__(*args, **strip_dict(kw, ['related_manager']))
        self.related_manager = kw.get('related_manager', None)

    def related_instance(self, validated_data):
        return (
            self.related_manager.create(**filter_dict(validated_data, self.__class__.Meta.instance_fields)) 
            if self.related_manager 
            else self.__class__.Meta.model.objects.create(**filter_dict(validated_data, self.__class__.Meta.instance_fields))
        )
        
    def create(self, validated_data):
        instance = self.related_instance(validated_data)
        if hasattr(self.__class__.Meta, 'related_fields'):
            for field, serializer_class, related_manager in self.__class__.Meta.related_fields:
                if related_manager:      
                    serializer = serializer_class(related_manager=getattr(instance, related_manager))
                else:
                    serializer = serializer_class()
                for data in validated_data.get(field, []):
                    serializer.create(data)
        return instance
    
