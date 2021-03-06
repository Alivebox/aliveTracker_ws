from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^groups/$', 'groups.views.groupsServices'),
                       url(r'^groups/allGroupsByUser', 'groups.views.getAllGroupsByUser'),
                       url(r'^groups/delete/(?P<argGroupID>[0-9]+)$', 'groups.views.deleteGroupProcess'),
                       url(r'^groups/getGroupsByUser/$', 'groups.views.getGroupsByUser'),
                       url(r'^groups/getGroupsByUser/$', 'groups.views.getGroupsByUser'),
                       url(r'^users/group/(?P<argGroupID>[0-9]+)$', 'groups.views.getUsersByGroup'),
                       url(r'^groups/getAllGroups/$', 'groups.views.getAllGroups'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)


