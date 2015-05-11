from django.conf.urls import include, patterns, url
from django.contrib import admin
from emp_info import views

urlpatterns = [
    # Examples:
    #url(r'^home/', 'usr_details.views.home_view', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^usr_details/', include('emp_info.urls')),
    url(r'^login/', 'emp_info.views.login_view', name='login'),
    url(r'^logout/', 'emp_info.views.logout_view', name='logout'),	
    url(r'^changep/(?P<id>\d+)/$', 'emp_info.views.changep_view', name='changep'),	
    url(r'^home/', 'emp_info.views.home_view', name='home'),
    url(r'^edit/(?P<id>\d+)/$', 'emp_info.views.edit_view', name='edit'),
    url(r'^edit/', 'emp_info.views.edit_view', name='editback'),	
    url(r'^admin/', include(admin.site.urls)),	
    #url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': ''})
]

