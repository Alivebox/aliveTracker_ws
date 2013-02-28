from rest_framework import serializers
from main.models import Project, User, Group
from projects.dtos import ProjectUserDTO
from main.utils import stringToDate


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
    fields = ('id', 'name', 'description', 'created', 'entity_status', 'group')
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(required=True,max_length=30)
    description = serializers.CharField(required=True,max_length=250)
    created = serializers.CharField(required=True,max_length=250)
    entity_status = serializers.IntegerField(default=0)
    group = serializers.PrimaryKeyRelatedField()

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance.
        """
        if instance:
            # Update existing instance
            instance.name = attrs.get('name', instance.name)
            instance.description = attrs.get('description', instance.description)
            instance.created = attrs.get('created', instance.created)
            instance.entity_status = attrs.get('entity_status', instance.entity_status)
            instance.group = (attrs.get('group', instance.group))
            return instance

        # Create new instance
        return Project(**attrs)


class ProjectUserDTOSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    project_id = serializers.IntegerField()
    role_id = serializers.IntegerField()
    username = serializers.CharField()
    rolename = serializers.CharField()

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.user_id = attrs['user_id']
            instance.group_id = attrs['group_id']
            instance.role_id = attrs['role_id']
            instance.username = attrs['username']
            instance.rolename = attrs['rolename']
            return instance
        return ProjectUserDTO(**attrs)