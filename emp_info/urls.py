from django.conf.urls import patterns, url

from emp_info import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
