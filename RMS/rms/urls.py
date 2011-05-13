from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from rms.views import ProductView, BacklogView, add_backlog

admin.autodiscover()

urlpatterns = patterns('',
                url(r'^$',ProductView.as_view(), name='product_index'),
                url(r'^product/$',ProductView.as_view(), name='product_index'),
                url(r'^backlog/$',BacklogView.as_view(), name='backlog_index'),
                (r'^backlog/(\d+)/$', BacklogView.as_view()),
                url(r'^add-backlog/$', add_backlog, name='backlog_add')

)
