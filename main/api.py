from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.serializers import Serializer
from main.models import Group
from main.models import Project


class GroupResource(ModelResource):
    class Meta:
        queryset = Group.objects.all()
        resource_name = 'group'
        authentication = Authentication()
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'put', 'delete', 'patch']
        serializer = Serializer(formats=['json'])

        # def dehydrate(self, bundle):
    #     bundle.data['success'] = True
    #     return bundle
    # def determine_format(self, request):
        #     return 'application/json'


class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'project'
        authentication = Authentication()
        authorization = Authorization()
        excludes = ['entity_status']
        allowed_methods = ['get', 'post', 'put', 'delete', 'patch']
        serializer = Serializer(formats=['json'])
