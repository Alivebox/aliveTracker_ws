from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^groups/$', 'groups.views.retrieveMyGroups'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)

