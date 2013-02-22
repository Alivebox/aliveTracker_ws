from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from main import views

urlpatterns = patterns('',
                       url(r'^main/(?P<id>[0-9]+)/$', 'main.views.user_authentication'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
