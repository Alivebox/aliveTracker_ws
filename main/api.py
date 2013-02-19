import copy
from tastypie.resources import ModelResource
from tastypie import fields
from winerror import ERROR_RESOURCE_NAME_NOT_FOUND

from main.models import Group

class GroupResource(ModelResource):
    class Meta:
        queryset = Group.objects.all()
    def dehydrate(self, bundle):
        bundle.data['success'] = True
        return bundle