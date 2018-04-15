from django.conf.urls import patterns, include, url
from django.contrib import admin

    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'cms.views.main'),
    url(r'^(.+)$', 'cms.views.get_page')
]
