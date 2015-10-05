from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Authentication
    ## Override logout next_page
    url(r'^accounts/logout/$',
        auth_views.logout,
        {'next_page': '/'},
        name='auth_logout'),
    url(r'^accounts/',
        include('registration.backends.hmac.urls')),

    # Backend urls
    url(r'^$',
        views.HomeView.as_view(),
        name='home'),
    url(r'^submit$',
        login_required(views.SubmitView.as_view()),
        name='submit'),
    url(r'^scores$',
        views.ScoreboardView.as_view(),
        name='scores'),
    url(r'^chals$',
        login_required(views.ChallengesView.as_view()),
        name='chals'),
    url(r'^chals/hint/(?P<buy_hint>[0-9]+)/buy',
        login_required(views.ChallengesView.as_view()),
        name='buy_hint'),
    #url(r'^stats$',
    #    views.StatisticsView.as_view(),
    #    name='stats'),
]
