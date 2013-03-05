from main.models import Project, Group
from main.utils import getPropertyByName


#Deserialize a project model
def projectDeserializer(argData):
    tmpProject = Project(name=getPropertyByName('name', argData.items()),
                         description=getPropertyByName('description', argData.items()),
                         created=getPropertyByName('created', argData.items()),
                         entity_status=0,
                         group=Group.objects.get(pk=getPropertyByName('group', argData.items())))
    return tmpProject
