from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^projects/group/(?P<argGroupID>[0-9]+)$', 'projects.views.getProjectsByUserAndGroup'),
                       url(r'^projects/getProject/$', 'projects.views.getProject'),
                       url(r'^projects/saveProject/(?P<argId>[0-9]+)$', 'projects.views.saveProject'),
                       # url(r'^projects/updateProjectsUserList', 'projects.views.updateProjectsUserList'),
)

urlpatterns = format_suffix_patterns(urlpatterns)