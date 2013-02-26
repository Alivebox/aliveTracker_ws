from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^', include('projects.urls')),
                       url(r'^', include('main.urls')),
                       url(r'^', include('groups.urls')),
                       )
