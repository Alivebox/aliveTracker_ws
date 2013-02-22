from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from main import views

urlpatterns = patterns('',
                       url(r'^main/(?P<email>[0-9]+)/$', views.User.as_view()),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)
