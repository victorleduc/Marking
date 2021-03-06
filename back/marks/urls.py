__author__ = 'Steven'


from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^myprojects$', views.myprojects, name='myprojects'),
    url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<project_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<project_id>[0-9]+)/editsec/$', views.editsec, name='editsec'),
    url(r'^(?P<project_id>[0-9]+)/deleteimg/(?P<pict_id>[0-9]+)/$', views.deleteimg, name='deleteimg'),
    # ex: /polls/5/mark/
    url(r'^(?P<project_id>[0-9]+)/mark/$', views.mark, name='grade'),
]

