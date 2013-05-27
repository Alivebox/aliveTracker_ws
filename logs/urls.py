from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^logs(/group/(?P<group>[0-9]+))?(/(?P<argLog>[0-9]+))?/$', 'logs.views.myLogsServices'),
                       url(r'^log/$', 'logs.views.create_log'),
                       url(r'^log/(?P<pk>[0-9]+)$', 'logs.views.update_log'),
                       url(r'^note/(?P<pk>[0-9]+)$', 'logs.views.delete_note'),
                       url(r'^log/notes/(?P<log>[0-9]+)$', 'logs.views.get_notes'),
                       url(r'^logs/exportReport/$', 'logs.views.exportReport'),
                       url(r'^logs/listReport/group/(?P<group>[0-9]+)/project/(?P<project>[0-9]+)/user/(?P<user>[0-9]+)/range/(?P<range>[0-4]+)/$', 'logs.views.listReport'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)

