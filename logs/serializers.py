from rest_framework import serializers
from main.models import Log

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
    fields = ('id', 'activity', 'time', 'date', 'user', 'project', 'group', 'entity_status')
    pk = serializers.Field()
    activity = serializers.CharField()
    time = serializers.IntegerField(default=0)
    date = serializers.CharField()
    user = serializers.CharField()
    project = serializers.CharField()
    group = serializers.CharField()
    entity_status = serializers.IntegerField(default=0)

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.activity = attrs.get('activity', instance.activity)
            instance.time = attrs.get('time', instance.time)
            instance.date = attrs.get('date', instance.date)
            instance.user = attrs.get('user', instance.user)
            instance.project = attrs.get('project', instance.project)
            instance.group = attrs.get('group', instance.group)
            instance.entity_status = attrs.get('entity_status', instance.entity_status)
            return instance

        return Log(**attrs)
