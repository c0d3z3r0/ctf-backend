"""ctfbackend URL Configuration

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
from django.contrib.auth import views as auth_views
import ctfbackend.backend.urls

urlpatterns = [
    # Authentication
    ## Override admin login site
    url(r'^admin/login/$', auth_views.login, name='auth_admin_login'),
    ## Set next_page for logout
    url(r'^admin/logout/$', auth_views.logout, {'next_page': '/'}),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(ctfbackend.backend.urls)),
]
