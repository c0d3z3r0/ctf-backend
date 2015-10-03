from django.conf.urls import url, include
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication
    ## Override logout next_page
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    ## Override use of uidb36 in django-registration
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        name='auth_password_reset_confirm'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),

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
