from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'SocialJunction.views.home', name='home'),
    url(r'^projects/', include('projects.urls')),
    url(r'^admin/', include(admin.site.urls)),     
)
