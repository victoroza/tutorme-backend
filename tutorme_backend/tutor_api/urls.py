from django.conf.urls import url
from tutor_api import views

urlpatterns= [
	url(r'^tutor_api/schools/$', 
		views.SchoolList.as_view(),
		name='school-list'),
    url(r'^tutor_api/schools/(?P<pk>[0-9]+)/$', 
    	views.SchoolDetail.as_view(),
    	name='school-detail'),
    url(r'^tutor_api/classes/$', 
    	views.ClassList.as_view(),
    	name='class-list'),
    url(r'^tutor_api/classes/(?P<pk>[0-9]+)/$', 
    	views.ClassDetail.as_view(),
    	name='class-detail'),
    url(r'^tutor_api/users/$', 
    	views.UserList.as_view(),
    	name='user-list'),
    url(r'^tutor_api/users/(?P<pk>[0-9]+)/$', 
    	views.UserDetail.as_view(),
    	name='user-detail'),
    url(r'^tutor_api/departments/$', 
    	views.DepartmentList.as_view(),
    	name='department-list'),
    url(r'^tutor_api/departments/(?P<shortName>.+)/$', 
    	views.DepartmentDetail.as_view(),
    	name='department-detail'),
]