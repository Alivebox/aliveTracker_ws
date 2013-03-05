from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
<<<<<<< HEAD
                       url(r'^projects/group/(?P<argGroupID>[0-9]+)$', 'projects.views.getProjectsByUserAndGroup'),
                       url(r'^projects/(?P<argProjectID>[0-9]+)$', 'projects.views.getProject'),
                       url(r'^projects/saveProject/$', 'projects.views.saveProject'),
                       url(r'^projects/deleteProject', 'projects.views.deleteProject'),
=======
                       url(r'^projects/retrieveUsersByProject/$', 'projects.views.retrieveUsersByProject'),
                       url(r'^projects/projectServices/$', 'projects.views.projectServices'),
                       url(r'^projects/projectServices/(?P<argId>[0-9]+)$', 'projects.views.deleteProject'),
                       # url(r'^projects/updateProjectsUserList', 'projects.views.updateProjectsUserList'),
>>>>>>> 284052432c8ed570e57f5bf9922f707336daf126
)

urlpatterns = format_suffix_patterns(urlpatterns)