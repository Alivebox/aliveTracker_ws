from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.serializers import Serializer
from main.models import Group


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