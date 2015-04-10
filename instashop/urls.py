from django.conf.urls import patterns, include, url

import views
# from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'instashop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.merhaba_dunya)
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()