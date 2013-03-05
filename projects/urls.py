from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^projects/group/(?P<argGroupID>[0-9]+)$', 'projects.views.getProjectsByUserAndGroup'),
                       url(r'^projects/(?P<argProjectID>[0-9]+)$', 'projects.views.getProject'),
                       url(r'^projects/saveProject/$', 'projects.views.saveProject'),
                       url(r'^projects/deleteProject', 'projects.views.deleteProject'),
)

urlpatterns = format_suffix_patterns(urlpatterns)