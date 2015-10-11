from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from .views import \
    RegistrationView, HomeView, SubmitView, ScoreboardView, ChallengesView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Authentication
    ## Override registration form
    url(r'^accounts/register/$',
        RegistrationView.as_view(),
        name='registration_register'),
    ## Override logout next_page
    url(r'^accounts/logout/$',
        auth_views.logout,
        {'next_page': '/'},
        name='auth_logout'),
    url(r'^accounts/',
        include('registration.backends.hmac.urls')),

    # Backend urls
    url(r'^$',
        HomeView.as_view(),
        name='home'),
    url(r'^submit$',
        login_required(SubmitView.as_view()),
        name='submit'),
    url(r'^scores$',
        ScoreboardView.as_view(),
        name='scores'),
    url(r'^chals$',
        login_required(ChallengesView.as_view()),
        name='chals'),
    url(r'^chals/hint/(?P<buy_hint>[0-9]+)/buy',
        login_required(ChallengesView.as_view()),
        name='buy_hint'),
    #url(r'^stats$',
    #    StatisticsView.as_view(),
    #    name='stats'),
]
