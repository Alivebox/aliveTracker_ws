from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

admin.autodiscover(),
urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^main/$', 'main.views.user_authentication'),
                       url(r'^main/retrieveAllUserRoles/$', 'main.views.retrieveAllUserRoles'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)

