from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^groups/$', 'groups.views.groupsServices'),
                       url(r'^groups/delete/(?P<argGroupID>[0-9]+)$', 'groups.views.deleteGroupProcess'),
                       url(r'^groups/getGroupsByUser/$', 'groups.views.getGroupsByUser'),
                       url(r'^groups/updateUser/$', 'groups.views.updateUserRole'),
                       url(r'^users/group/(?P<argGroupID>[0-9]+)$', 'groups.views.getUsersByGroup'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)


