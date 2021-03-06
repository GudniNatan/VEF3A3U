"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from routing import urls as routing_urls
from MVC import urls as MVC_urls
from lokaverkefni import urls as lokaverkefni_urls


urlpatterns = [
    url(r'^(?i)admin/', include(admin.site.urls)),
    url(r'^(?i)MVC/', include(MVC_urls, namespace='MVC', app_name='MVC')), #This is how app urls should be
    url(r'^(?i)routing/', include(routing_urls)),
    url(r'^(?i)lokaverkefni/', include(lokaverkefni_urls)),
]