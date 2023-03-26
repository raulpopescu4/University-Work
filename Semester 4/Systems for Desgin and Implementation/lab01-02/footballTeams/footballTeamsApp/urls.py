from . import views
from django.urls import path, include
from .views import FootballLeagueList, FootballLeagueDetail, FootballTeamList, FootballTeamDetail

urlpatterns = [
    path('', views.home, name="home"),
    path('football_league/', FootballLeagueList.as_view()),
    path('football_league/<int:pk>/', FootballLeagueDetail.as_view()),
    path('football_team/', FootballTeamList.as_view()),
    path('football_team/<int:pk>/', FootballTeamDetail.as_view()),
]
