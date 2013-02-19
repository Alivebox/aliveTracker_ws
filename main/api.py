import copy
from tastypie.resources import ModelResource
from tastypie import fields

from main.models import Group

class GroupResource(ModelResource):
    class Meta:
        queryset = Group.objects.all()
        resourcename = 'groups'
    # def dehydrate(self, bundle):
    #     bundle.data['success'] = True
    #     return bundle
    def determine_format(self, request):
        return 'application/json'