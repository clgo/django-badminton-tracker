from django.conf.urls import url
from login import views

urlpatterns = [
	url(r'^$', views.LoginView.as_view(), name='login'),
	url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]