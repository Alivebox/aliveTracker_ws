from datetime import date
from main.models import Project, Group
from main.utils import getPropertyByName


def projectDeserializer(argData, argGroupID):
    tmpProject = Project(name=getPropertyByName('name', argData.items()),
                         description=getPropertyByName('description', argData.items()),
                         created=getPropertyByName('created', date.today()),
                         entity_status=0,
                         group=Group.objects.get(argGroupID))
    return tmpProject