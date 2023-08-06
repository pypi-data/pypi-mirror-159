# -*- coding: utf-8
from django.conf.urls import include
from django.urls import re_path
from .compat import admin_urls


urlpatterns = [
    re_path(r'^admin/', admin_urls),
    re_path(r'^', include('compliant_social_django.urls', namespace='social')),
]
