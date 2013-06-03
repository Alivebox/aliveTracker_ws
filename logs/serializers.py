from rest_framework import serializers
from main.models import Log, Note
from logs.dtos import LogGroupProjectDateDTO


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


class LogGroupProjectDateDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    activity = serializers.CharField()
    time = serializers.FloatField(default=0)
    date = serializers.CharField()
    user = serializers.IntegerField(default=0)
    project = serializers.IntegerField()
    project_name = serializers.CharField()
    group = serializers.IntegerField()

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.id = attrs['id']
            instance.activity = attrs['activity']
            instance.time = attrs['time']
            instance.date = attrs['date']
            instance.user = attrs['user_id']
            instance.project = attrs['project_id']
            instance.project_name = attrs['project_name']
            instance.group = attrs['group_id']
            return instance
        return LogGroupProjectDateDTO(**attrs)


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
    fields = ('id', 'note')
    pk = serializers.Field()
    note = serializers.IntegerField()
    entity_status = serializers.IntegerField(default=0)

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.note = attrs.get('note', instance.user)
            instance.entity_status = attrs.get('entity_status', instance.entity_status)
            return instance

        return Note(**attrs)