from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

admin.autodiscover(),
urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^main/$', 'main.views.user_authentication'),
                       url(r'^main/permissions/$', 'main.views.user_permissions'),
                       url(r'^main/register/$', 'main.views.register_user'),
                       url(r'^main/user/(?P<pk>[0-9]+)$', 'main.views.update_user'),
                       )

urlpatterns = format_suffix_patterns(urlpatterns)

