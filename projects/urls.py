from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^projects/retrieveUsersByProject/$', 'projects.views.retrieveUsersByProject'),
                       url(r'^projects/projectServices/$', 'projects.views.projectServices'),
                       url(r'^projects/projectServices/(?P<argId>[0-9]+)$', 'projects.views.deleteProject'),
                       # url(r'^projects/updateProjectsUserList', 'projects.views.updateProjectsUserList'),
)

urlpatterns = format_suffix_patterns(urlpatterns)