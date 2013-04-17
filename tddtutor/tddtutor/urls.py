from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tddtutor.views.home', name='home'),
    # url(r'^tddtutor/', include('tddtutor.foo.urls')),
    url(r'^polls/$', 'polls.views.show_all_pools'),
    url(r'^poll/(?P<poll_id>\d+)$', 'polls.views.poll'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
