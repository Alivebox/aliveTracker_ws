from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns(
    url(r'^main/retrieveUsersByProject', 'projects.views.retrieveUsersByProject'),
    url(r'^main/addNewProjectToGroup', 'projects.views.addNewProjectToGroup'),
    url(r'^main/updateProject', 'projects.views.updateProject'),
    url(r'^main/deleteProject', 'projects.views.deleteProject'),
    url(r'^main/updateProjectsUserList', 'projects.views.updateProjectsUserList'),
    )

urlpatterns = format_suffix_patterns(urlpatterns)