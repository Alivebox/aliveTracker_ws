from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^logs/$', 'groups.views.myLogsServices'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)