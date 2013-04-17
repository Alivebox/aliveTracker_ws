from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

admin.autodiscover(),
urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^main/$', 'main.views.user_authentication'),
                       url(r'^main/user/$', 'main.views.getUserAuth'),
                       url(r'^main/(?P<pk>[0-9]+)?$', 'main.views.user_services'),
                       url(r'^main/permissions/group/(?P<pk>[0-9]+)$', 'main.views.user_permissions'),
                       url(r'^main/register/$', 'main.views.register_user'),
                       url(r'^main/user/(?P<pk>[0-9]+)$', 'main.views.update_user'),
                       url(r'^main/user/group/(?P<group>[0-9]+)/project/(?P<project>[0-9]+)$', 'main.views.getUserByGroupAndProject'),
                       url(r'^main/forgotPassword/$', 'main.views.forgotPassword'),
                       url(r'^main/resetPassword/(?P<email>(([A-Za-z0-9]+)|([A-Za-z0-9]+\.[A-Za-z0-9]+))@[A-Za-z0-9]+(\.[A-Za-z]{2,4}){1,2})/(?P<token>[A-Za-z0-9]+)$', 'main.views.resetPassword'),
                       url(r'^main/users/(?P<argEmail>(([A-Za-z0-9]+)|([A-Za-z0-9]+\.[A-Za-z0-9]+)))$', 'main.views.getUsers'),
                       url(r'^main/users2/(?P<argEmail>(([A-Za-z0-9]+)|([A-Za-z0-9]+\.[A-Za-z0-9]+))}@[A-Za-z0-9]+(\.[A-Za-z]{2,4}){1,2})$', 'main.views.getUsers'),
                       url(r'^roles/', 'main.views.getRoles'),
                       url(r'^main/users/delete/(?P<argUserID>[0-9]+)/group/(?P<argGroupID>[0-9]+)$', 'main.views.deleteUser')
                       )

urlpatterns = format_suffix_patterns(urlpatterns)

