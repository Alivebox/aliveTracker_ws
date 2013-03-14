from rest_framework import serializers
from main.models import Project
from projects.dtos import ProjectUserListDTO, UserDTO


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'created', 'entity_status', 'group')
        name = serializers.CharField(required=True,max_length=30)
        description = serializers.CharField(required=True,max_length=250)
        created = serializers.CharField(required=True,max_length=250)
        entity_status = serializers.IntegerField(default=0)
        group = serializers.PrimaryKeyRelatedField()


class ProjectUserListDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.IntegerField()
    created = serializers.IntegerField()
    description = serializers.CharField()
    groupID = serializers.CharField()
    users = serializers.CharField()

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.id = attrs['id']
            instance.name = attrs['name']
            instance.created = attrs['created']
            instance.description = attrs['description']
            instance.groupID = attrs['groupID']
            instance.users = attrs['users']
            return instance
        return ProjectUserListDTO(**attrs)


class userListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    role = serializers.CharField()

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.id = attrs['id']
            instance.name = attrs['name']
            instance.role = attrs['role']
            return instance
        return UserDTO(**attrs)