from tastypie.resources import ModelResource
from main.models import Group


class GroupResource(ModelResource):
    class Meta:
        queryset = Group.objects.all()
        resource_name = 'group'
    # def dehydrate(self, bundle):
    #     bundle.data['success'] = True
    #     return bundle
    def determine_format(self, request):
        return 'application/json'