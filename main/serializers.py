from rest_framework import serializers
from main.models import User, Group_User, Role


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
    fields = ('id', 'name', 'email', 'password', 'entity_status')
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(required=True,max_length=50)
    email = serializers.CharField(max_length=50)
    password = serializers.CharField(required=True, max_length=20)
    entity_status = serializers.IntegerField(default=0)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance.
        """
        if instance:
            # Update existing instance
            instance.name = attrs.get('name', instance.name)
            instance.email = attrs.get('email', instance.email)
            instance.password = attrs.get('password', instance.password)
            instance.entity_status = attrs.get('entity_status', instance.entity_status)
            return instance

        # Create new instance
        return User(**attrs)


class GroupUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group_User
    fields = ('id', 'user', 'group', 'role')
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    user = serializers.CharField(required=True,max_length=50)
    role = serializers.CharField(max_length=50)
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


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
    fields = ('id', 'name', 'description', 'entity_status')
    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    name = serializers.CharField(required=True,max_length=30)
    description = serializers.CharField(required=True,max_length=250)
    entity_status = serializers.IntegerField(default=0)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance.
        """
        if instance:
            # Update existing instance
            instance.name = attrs.get('name', instance.name)
            instance.description = attrs.get('description', instance.description)
            instance.entity_status = attrs.get('entity_status', instance.entity_status)
            return instance

        # Create new instance
        return User(**attrs)