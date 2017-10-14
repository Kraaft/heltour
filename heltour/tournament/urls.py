"""heltour2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from . import views, api, android_app, auth
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.cache import cache_control

season_urlpatterns = [
    url(r'^summary/$', views.SeasonLandingView.as_view(), name='season_landing'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^registration_success/$', views.RegistrationSuccessView.as_view(), name='registration_success'),
    url(r'^rosters/$', views.RostersView.as_view(), name='rosters'),
    url(r'^standings/$', views.StandingsView.as_view(), name='standings'),
    url(r'^standings/section/(?P<section>[\w-]+)/$', views.StandingsView.as_view(), name='standings_by_section'),
    url(r'^crosstable/$', views.CrosstableView.as_view(), name='crosstable'),
    url(r'^wallchart/$', views.WallchartView.as_view(), name='wallchart'),
    url(r'^pairings/$', views.PairingsView.as_view(), name='pairings'),
    url(r'^pairings/calendar.ics$', views.ICalPairingsView.as_view(), name='pairings_icalendar'),
    url(r'^pairings/team/(?P<team_number>[0-9]+)/$', views.PairingsView.as_view(), name='pairings_by_team'),
    url(r'^pairings/team/(?P<team_number>[0-9]+)/calendar.ics$', views.ICalPairingsView.as_view(), name='pairings_by_team_icalendar'),
    url(r'^round/(?P<round_number>[0-9]+)/pairings/$', views.PairingsView.as_view(), name='pairings_by_round'),
    url(r'^round/(?P<round_number>[0-9]+)/pairings/team/(?P<team_number>[0-9]+)/$', views.PairingsView.as_view(), name='pairings_by_round_team'),
    url(r'^stats/$', views.StatsView.as_view(), name='stats'),
    url(r'^dashboard/$', staff_member_required(views.LeagueDashboardView.as_view()), name='league_dashboard'),
    url(r'^player/$', views.UserDashboardView.as_view(), name='user_dashboard'),
    url(r'^player/(?P<username>[\w-]+)/$', views.PlayerProfileView.as_view(), name='player_profile'),
    url(r'^team/(?P<team_number>[0-9]+)/$', views.TeamProfileView.as_view(), name='team_profile'),
    url(r'^tv/$', cache_control(no_cache=True)(views.TvView.as_view()), name='tv'),
    url(r'^tv/json/$', cache_control(no_cache=True)(views.TvJsonView.as_view()), name='tv_json'),
    url(r'^document/(?P<document_tag>[\w-]+)/$', views.DocumentView.as_view(), name='document'),
    url(r'^request/(?P<req_type>\w+)/$', views.ModRequestView.as_view(), name='modrequest'),
    url(r'^request/(?P<req_type>\w+)/success/$', views.ModRequestSuccessView.as_view(), name='modrequest_success'),
    url(r'^nominate/$', views.NominateView.as_view(), name='nominate'),
    url(r'^nominate/delete/(?P<nomination_id>\w+)/$', views.DeleteNominationView.as_view(), name='delete_nomination'),
    url(r'^schedule/edit/$', views.ScheduleView.as_view(), name='edit_schedule'),
    url(r'^availability/edit/$', views.AvailabilityView.as_view(), name='edit_availability'),
    url(r'^board/(?P<board_number>[0-9]+)/scores/$', views.BoardScoresView.as_view(), name='board_scores'),
    url(r'^alternates/$', views.AlternatesView.as_view(), name='alternates'),
    url(r'^round/(?P<round_number>[0-9]+)/alternate/accept/$', views.AlternateAcceptView.as_view(), name='alternate_accept'),
    url(r'^round/(?P<round_number>[0-9]+)/alternate/decline/$', views.AlternateDeclineView.as_view(), name='alternate_decline'),
    url(r'^notifications/$', views.NotificationsView.as_view(), name='notifications'),
]

league_urlpatterns = [
    url(r'^$', views.LeagueHomeView.as_view(), name='league_home'),
    url(r'^', include(season_urlpatterns)),
    url(r'^season/(?P<season_tag>[\w-]+)/', include(season_urlpatterns, 'by_season')),
    url(r'^document/(?P<document_tag>[\w-]+)/$', views.DocumentView.as_view(), name='document'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^contact_success/$', views.ContactSuccessView.as_view(), name='contact_success'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^login/(?P<secret_token>\w+)/$', views.LoginView.as_view(), name='login_with_token'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]

api_urlpatterns = [
    url(r'^find_pairing/$', api.find_pairing, name='find_pairing'),
    url(r'^update_pairing/$', api.update_pairing, name='update_pairing'),
    url(r'^get_roster/$', api.get_roster, name='get_roster'),
    url(r'^assign_alternate/$', api.assign_alternate, name='assign_alternate'),
    url(r'^set_availability/$', api.set_availability, name='set_availability'),
    url(r'^get_league_moderators/$', api.get_league_moderators, name='get_league_moderators'),
    url(r'^league_document/$', api.league_document, name='league_document'),
    url(r'^link_slack/$', api.link_slack, name='link_slack'),
    url(r'^get_slack_user_map/$', api.get_slack_user_map, name='get_slack_user_map'),
    url(r'^game_warning/$', api.game_warning, name='game_warning'),
    url(r'^player_contact/$', api.player_contact, name='player_contact'),
]

app_urlpatterns = [
    url(r'^event/$', android_app.slack_event, name='slack_event'),
    url(r'^register/$', android_app.fcm_register, name='fcm_register'),
    url(r'^unregister/$', android_app.fcm_unregister, name='fcm_unregister'),
]

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^player/(?P<username>[\w-]+)/calendar.ics$', views.ICalPlayerView.as_view(), name='player_icalendar'),
    url(r'^api/', include(api_urlpatterns, 'api')),
    url(r'^app/', include(app_urlpatterns, 'app')),
    url(r'^auth/slack/$', auth.SlackAuth.as_view(), name='slack_auth'),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^select2/', include('select2.urls')),
    url(r'^(?P<league_tag>[\w-]+)/', include(league_urlpatterns, 'by_league')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
