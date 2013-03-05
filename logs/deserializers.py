from main.models import Project, Group, Log, User
from main.utils import getPropertyByName


def logDeserializer(argData):
    tmpLog =  Log(activity=getPropertyByName('activity', argData.items()),
                  time=getPropertyByName('time', argData.items()),
                  date=getPropertyByName('date', argData.items()),
                  user=User.objects.get(pk=getPropertyByName('user', argData.items())),
                  project=Project.objects.get(pk=getPropertyByName('project', argData.items())),
                  group=Group.objects.get(pk=getPropertyByName('group', argData.items())),
                  entity_status=0)
    return tmpLog