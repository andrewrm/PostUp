from django.conf.urls import patterns, include, url
from tastypie.api import Api

from core.api import PostAccountResource, GeoPostResource

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


api_resource = Api(api_name='myApi')
api_resource.register(PostAccountResource())
api_resource.register(GeoPostResource())



urlpatterns = patterns('core.views',
    # Examples:
    # url(r'^$', 'argos.views.home', name='home'),
    url(r'^/?$', 'home', name='home'),
    url(r'^about/?$', 'about', name='about'),
    url(r'^contact/?$', 'contact', name='contact'),
    url(r'^api/', include(api_resource.urls))

    
    # url(r'^argos/', include('argos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
