from rest_framework import serializers
from main.models import Project
from main.models import User
from main.utils import dateToString


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
    fields = ('id', 'name', 'description', 'created', 'entity_status', 'group')
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(required=True,max_length=30)
    description = serializers.CharField(required=True,max_length=250)
    created = serializers.CharField(required=True,max_length=250)
    entity_status = serializers.IntegerField(default=0)
    group = serializers.Field()

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance.
        """
        if instance:
            # Update existing instance
            instance.name = attrs.get('name', instance.name)
            instance.description = attrs.get('description', instance.description)
            instance.created = attrs.get('created', dateToString(instance.created))
            instance.entity_status = attrs.get('entity_status', instance.entity_status)
            return instance

        # Create new instance
        return User(**attrs)
        