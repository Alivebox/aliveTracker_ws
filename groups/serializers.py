from rest_framework import serializers
from main.models import Group, Group_User, Log


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
    fields = ('id', 'name', 'description', 'logo_url', 'web_site_url','created','entity_status')
    pk = serializers.Field()
    name = serializers.CharField(required=True,max_length=50)
    description = serializers.CharField(max_length=200)
    logo_url = serializers.CharField(required=True,max_length=50)
    web_site_url = serializers.CharField(required=True,max_length=50)
    created = serializers.IntegerField(default=0)
    entity_status = serializers.IntegerField(default=0)

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.name = attrs.get('name', instance.name)
            instance.description = attrs.get('description', instance.description)
            instance.logo_url = attrs.get('logo_url', instance.logo_url)
            instance.web_site_url = attrs.get('web_site_url', instance.web_site_url)
            instance.created = attrs.get('created', instance.created)
            instance.entity_status = attrs.get('entity_status', instance.entity_status)
            return instance

        # Create new instance
        return Group(**attrs)


class Group_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group_User
    fields = ('id', 'user_id', 'group_id', 'role_id')
    pk = serializers.Field()
    user = serializers.IntegerField()
    group = serializers.IntegerField()
    role = serializers.IntegerField()

    def restore_object(self, attrs, instance=None):
        if instance:
            # Update existing instance
            instance.user = attrs.get('user', instance.user)
            instance.group = attrs.get('group', instance.group)
            instance.role = attrs.get('role', instance.role)
            return instance

        # Create new instance
        return Group_User(**attrs)


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
    fields = ('id', 'activity', 'time', 'date', 'user', 'project', 'group')
    pk = serializers.Field()
    activity = serializers.Field
    time = serializers.Field
    date = serializers.CharField
    user = serializers.IntegerField()
    project = serializers.IntegerField()
    group = serializers.IntegerField()
    entity_status = serializers.IntegerField()

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.activity = attrs.get('activity', instance.activity)
            instance.time = attrs.get('time', instance.time)
            instance.date = attrs.get('date', instance.date)
            instance.user = attrs.get('user', instance.user_id)
            instance.project = attrs.get('project', instance.project_id)
            instance.group = attrs.get('group', instance.group)
            instance.entity_status = attrs.get('entity_status', instance.entity_status)
            return instance

        return Group_User(**attrs)