from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

admin.autodiscover(),
urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^main/$', 'main.views.header_caption'),
                       url(r'^main/(?P<password>[a-zA-Z0-9._%+-]{8,20})/(?P<email>(([A-Za-z0-9]+)|([A-Za-z0-9]+\.[A-Za-z0-9]+))@[A-Za-z0-9]+\.[A-Za-z]{2,4})/$', 'main.views.user_authentication')
                       )

urlpatterns = format_suffix_patterns(urlpatterns)

