from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    url(r'^$', views.base, name='base'),
    url(r'^djangogirls$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^heykorean_jobs$', views.heykorean_jobs, name='heykorean_jobs'),
    url(r'^jobkorea_jobs$', views.jobkorea_jobs, name='jobkorea_jobs'),

]