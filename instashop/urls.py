from django.conf.urls import patterns, include, url

import views
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'instashop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.merhaba_dunya),
    url(r'^panel/', include('panel.urls', namespace="panel")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'instashop.views.login'),
    url(r'^accounts/auth/$', 'instashop.views.auth_view'),
    url(r'^accounts/logout/$', 'instashop.views.logout'),
    url(r'^accounts/$', 'instashop.views.loggedin'),
    url(r'^accounts/invalid/$', 'instashop.views.invalid_login'),

    # url(r'accounts/login/$','django.contrib.auth.views.login', {'template_name':'panel/login.html'}),
    # url(r'accounts/logout/$','django.contrib.auth.views.logout', {'next_page':'/accounts/login/'}),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()