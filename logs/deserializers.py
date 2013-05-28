from main.models import Project, Group, Log, User, Note
from main.utils import getPropertyByName, getUserByRequest


def logDeserializer(argData, argUser, argDate):
    tmpLog = Log(activity=getPropertyByName('activity', argData.items()),
                 time=getPropertyByName('time', argData.items()),
                 date=argDate,
                 user=argUser,
                 project=Project.objects.get(pk=getPropertyByName('project', argData.items())),
                 group=Group.objects.get(pk=getPropertyByName('group', argData.items())),
                 entity_status=0)
    return tmpLog


def noteDeserializer(argData):
    tmpNote = Note(note=getPropertyByName('note', argData.items()),
                   log=Log.objects.get(pk=getPropertyByName('log', argData.items())),
                   entity_status=0)
    return tmpNote