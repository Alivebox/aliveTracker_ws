# urls.py
from django.conf.urls import *
from main.api import GroupResource
from main.api import ProjectResource
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(GroupResource())
v1_api.register(ProjectResource())
urlpatterns = patterns('',
                       #(r'^api/', include(story_resource.urls)),
                       (r'^api/', include(v1_api.urls)),
                       )

