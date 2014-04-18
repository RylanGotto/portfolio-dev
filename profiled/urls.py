from django.conf.urls import patterns, include, url
from blog import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'profiled.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home ,name="home"),
    url(r'^blog/', views.blog ,name="blog"),
    url(r'^(?P<slug>[\w\-]+)/$', views.getpost, name="getpost"),
)
