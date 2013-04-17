from rest_framework import serializers
from main.models import User, Group_User, Role
from main.dtos import PermissionGroupDTO, UserDTO, UserLoginDTO


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
    fields = ('id', 'name', 'email', 'entity_status')
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(required=True,max_length=50)
    email = serializers.CharField(max_length=50)
    entity_status = serializers.IntegerField(default=0)

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.name = attrs.get('name', instance.name)
            instance.email = attrs.get('email', instance.email)
            instance.entity_status = attrs.get('entity_status', instance.entity_status)
            return instance

        # Create new instance
        return User(**attrs)

class UserSerializerDTO(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.CharField()
    name = serializers.CharField()
    entity_status = serializers.IntegerField()

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.id = attrs['id']
            instance.email = attrs['email']
            instance.name = attrs['name']
            instance.entity_status = attrs['entity_status']
            return instance
        return UserLoginDTO(**attrs)


class GroupUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group_User
    fields = ('id', 'user', 'group', 'role')
    pk = serializers.Field()
    user = serializers.IntegerField()
    group = serializers.IntegerField()
    role = serializers.IntegerField()
    entity_status = serializers.IntegerField(default=0)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance.
        """
        if instance:
            # Update existing instance
            instance.user = attrs.get('user', instance.user)
            instance.group = attrs.get('group', instance.group)
            instance.role = attrs.get('role', instance.role)
            instance.entity_status = attrs.get('entity_status', instance.entity_status)
            return instance

        # Create new instance
        return Group_User(**attrs)


class PermissionGroupDTOSerializer(serializers.Serializer):
    idPermission = serializers.IntegerField()
    namePermission = serializers.CharField()

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.idPermission = attrs['idPermission']
            instance.namePermission = attrs['namePermission']
            return instance
        return PermissionGroupDTO(**attrs)


class UserDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.CharField()
    role_id = serializers.IntegerField()

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.id = attrs['id']
            instance.email = attrs['email']
            instance.role_id = attrs['role_id']
            return instance
        return UserDTO(**attrs)


class UserForgotPasswordSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    token = serializers.CharField()

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.user = attrs['user']
            instance.token = attrs['token']
            return instance
        return UserForgotPasswordSerializer(**attrs)


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
    fields = ('id', 'name', 'description', 'entity_status')
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(required=True,max_length=50)
    description = serializers.CharField(max_length=50)
    entity_status = serializers.IntegerField(default=0)

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.name = attrs.get('name', instance.name)
            instance.description = attrs.get('description', instance.email)
            instance.entity_status = attrs.get('entity_status', instance.entity_status)
            return instance

        # Create new instance
        return Role(**attrs)