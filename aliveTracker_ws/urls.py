from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from main.api import GroupResource

admin.autodiscover()

group_resource = GroupResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aliveTracker_ws.views.home', name='home'),
    # url(r'^aliveTracker_ws/', include('aliveTracker_ws.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(group_resource.urls)),
)
