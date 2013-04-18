from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^logs(/group/(?P<group>[0-9]+))?/$', 'logs.views.myLogsServices'),
                       url(r'^logs/exportReport/$', 'logs.views.exportReport'),
                       url(r'^logs/listReport/group/(?P<group>[0-9]+)/project/(?P<project>[0-9]+)/user/(?P<user>[0-9]+)/range/(?P<range>[0-4]+)?/$', 'logs.views.listReport'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)