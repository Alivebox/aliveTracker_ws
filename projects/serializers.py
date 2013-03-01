from rest_framework import serializers
from main.models import Project, Group
from projects.dtos import ProjectUserDTO


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'created', 'entity_status')
        name = serializers.CharField(required=True,max_length=30)
        description = serializers.CharField(required=True,max_length=250)
        created = serializers.CharField(required=True,max_length=250)
        entity_status = serializers.IntegerField(default=0)
        group = serializers.PrimaryKeyRelatedField()


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