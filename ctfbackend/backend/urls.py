from django.conf.urls import url, include
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url('^', include('django.contrib.auth.urls')),

    # Chrome favicon fix
    url(r'^favicon.png$', lambda x: HttpResponseRedirect(
        settings.STATIC_URL + 'backend/favicon.png')),

    # Backend urls
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^submit$', views.SubmitView.as_view(), name='submit'),
    url(r'^scores$', views.ScoreboardView.as_view(), name='scores'),
    url(r'^chals$', views.ChallengesView.as_view(), name='chals'),
    url(r'^chals/hint/(?P<buy_hint>[0-9]+)/buy', views.ChallengesView.as_view(), name='buy_hint'),
    url(r'^stats$', views.StatisticsView.as_view(), name='stats'),
]
