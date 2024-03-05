from . import views
from django.urls import path, re_path, include
from .views import *
from rest_framework_swagger.views import get_swagger_view
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Jaseci API",
        default_version='v1',
        description="Welcome to the world of Jaseci",
        terms_of_service="https://www.jaseci.org",
        contact=openapi.Contact(email="jason@jaseci.org"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'), 
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),  
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
    path('', views.home, name="home"),
    path('football_league/', FootballLeagueList.as_view()),
    path('football_league/<int:pk>/', FootballLeagueDetail.as_view()),
    path('football_team/', FootballTeamList.as_view()),
    path('football_team/<int:pk>/', FootballTeamDetail.as_view()),
    path('football_player/', FootballPlayerList.as_view()),
    path('football_player/<int:pk>/', FootballPlayerDetail.as_view()),
    path('competition/', CompetitionList.as_view()),
    path('competition/<int:pk>', CompetitionDetail.as_view()),
    path('competes_in/', CompetesInList.as_view()),
    path('competes_in/<int:pk>', CompetesInDetail.as_view()),
    path('avg_age_statistics/', AverageAgeTeamsView.as_view()),
    path('teams_by_number_of_players/', TeamsNumberOfPlayersView.as_view()),

]
