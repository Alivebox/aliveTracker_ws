from django.conf.urls import patterns, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^groups/(?P<password>[a-zA-Z0-9._%+-]{8,20})/(?P<userID>[a-z0-9_-]{8,20})/(?P<userName>[a-z0-9_-]{8,20})/$', 'groups.views.retrieveMyGroups'),
                       url(r'^groups/groupsIBelongTo/$', 'groups.views.retrieveGroupsIBelongTo'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)

