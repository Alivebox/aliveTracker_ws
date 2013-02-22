from django.forms import widgets
from rest_framework import serializers
from main.models import User


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