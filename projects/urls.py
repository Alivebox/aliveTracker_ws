from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^projects/group/(?P<argGroupID>[0-9]+)$', 'projects.views.getProjectsByUserAndGroup'),
                       url(r'^projects/(?P<argProjectID>[0-9]+)$', 'projects.views.getUserProjectByGroup'),
                       url(r'^projects/saveProject/(?P<argGroupId>[0-9]+)$', 'projects.views.saveProject'),
                       url(r'^projects/deleteProject/(?P<argProjectID>[0-9]+)$', 'projects.views.deleteProject'),
                       url(r'^projects/getProjectByUser', 'projects.views.getAllProjectsByUser'),
                       url(r'^projects/getProjectsByGroup/(?P<argGroupId>[0-9]+)$', 'projects.views.getProjectsByGroup'),
                       url(r'^projects/addUserProject/(?P<argProjectID>[0-9]+)/user/(?P<argUserId>[0-9]+)$','projects.views.saveUserProject'),
                       url(r'^projects/deleteUserProject/(?P<argProjectId>[0-9]+)/user/(?P<argUserId>[0-9]+)$', 'projects.views.deleteUserProject'),
                       url(r'^projects/getAllProjects/$', 'projects.views.getAllProjects'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)