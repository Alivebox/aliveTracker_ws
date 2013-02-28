from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^groups/$', 'groups.views.myGroupsServices'),
                       url(r'^groups/retrieveGroupsIBelongTo/$', 'groups.views.retrieveGroupsIBelongTo'),
                       url(r'^groups/addLogEntry/$', 'groups.views.addLogEntry'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)

