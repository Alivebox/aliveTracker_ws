from rest_framework import serializers
<<<<<<< HEAD
from main.models import Project
from projects.dtos import ProjectUserListDTO, UserDTO
=======
from main.models import Project, Group
from projects.dtos import ProjectUserDTO
>>>>>>> 284052432c8ed570e57f5bf9922f707336daf126


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
<<<<<<< HEAD
        fields = ('id', 'name', 'description', 'created', 'entity_status', 'group')
        id = serializers.IntegerField(default=0)
=======
        fields = ('name', 'description', 'created', 'entity_status')
>>>>>>> 284052432c8ed570e57f5bf9922f707336daf126
        name = serializers.CharField(required=True,max_length=30)
        description = serializers.CharField(required=True,max_length=250)
        created = serializers.CharField(required=True,max_length=250)
        entity_status = serializers.IntegerField(default=0)
        group = serializers.PrimaryKeyRelatedField()


<<<<<<< HEAD
class userListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.CharField()
    roleId = serializers.IntegerField()
=======
class ProjectUserDTOSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    project_id = serializers.IntegerField()
    role_id = serializers.IntegerField()
    username = serializers.CharField()
    rolename = serializers.CharField()
>>>>>>> 284052432c8ed570e57f5bf9922f707336daf126

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.id = attrs['id']
            instance.email = attrs['email']
            instance.roleId = attrs['roleId']
            return instance
<<<<<<< HEAD
        return UserDTO(**attrs)


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
=======
        return ProjectUserDTO(**attrs)
>>>>>>> 284052432c8ed570e57f5bf9922f707336daf126
