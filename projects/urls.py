from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^projects/retrieveAllProjectsByGroup/$', 'projects.views.retrieveAllProjectsByGroup'),
                       # url(r'^projects/retrieveUsersByProject', 'projects.views.retrieveUsersByProject'),
                       # url(r'^projects/addNewProjectToGroup', 'projects.views.addNewProjectToGroup'),
                       # url(r'^projects/updateProject', 'projects.views.updateProject'),
                       # url(r'^projects/deleteProject', 'projects.views.deleteProject'),
                       # url(r'^projects/updateProjectsUserList', 'projects.views.updateProjectsUserList'),
)

urlpatterns = format_suffix_patterns(urlpatterns)