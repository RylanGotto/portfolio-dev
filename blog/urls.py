from django.conf.urls import patterns, url
from blog import views


urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^(?P<slug>[\w\-]+)/$', views.getpost, name="getpost"),
	)