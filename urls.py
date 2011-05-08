from django.conf.urls.defaults import patterns, include, url
from casestudy.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     (r'^hello/$', hello),
     (r'^time/$',current_datetime),
     (r'^time/plus/(\d{1,2})/$', hours_ahead),
    # Examples:
    # url(r'^$', 'Study.views.home', name='home'),
    # url(r'^Study/', include('Study.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
