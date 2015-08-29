from django.conf.urls import url
from django.http import HttpResponseRedirect
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),

    # Chrome favicon fix
    url(r'^favicon.png$', lambda x: HttpResponseRedirect(
        settings.STATIC_URL + 'backend/favicon.png')),
]
