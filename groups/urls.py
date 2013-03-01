from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^groups/$', 'groups.views.myGroupsServices'),
                       url(r'^groups/groupsIBelong/$', 'groups.views.groupsIBelongServices'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)

