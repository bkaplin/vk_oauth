from django.conf.urls import patterns, include, url
from django.contrib import admin
from my_project import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url('', include('social_django.urls')),
    url(r'^logout/$', views.logout),
)