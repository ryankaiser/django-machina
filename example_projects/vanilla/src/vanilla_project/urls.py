# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from machina.app import board

from vanilla_project.views import UserAccountParametersUpdateView
from vanilla_project.views import UserPasswordUpdateView
from vanilla_project.views import UserCreateView
from vanilla_project.views import UserDeleteView


# Admin autodiscover
admin.autodiscover()

# Patterns
urlpatterns = [
    # Admin
    url(r'^' + settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^account/parameters/edit/',
        UserAccountParametersUpdateView.as_view(), name='account-parameters'),
    url(r'^account/password/edit/', UserPasswordUpdateView.as_view(), name='account-password'),
    url(r'^register/', UserCreateView.as_view(), name='register'),
    url(r'^unregister/', UserDeleteView.as_view(), name='unregister'),

    # Apps
    url(r'', include(board.urls)),
]

# In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    import debug_toolbar
    from django.views.static import serve
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += [
        url(r'^%s/(?P<path>.*)$' % media_url, serve, {'document_root': settings.MEDIA_ROOT}),
    ]
