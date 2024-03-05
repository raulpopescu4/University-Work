from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg, F, Count

from .models import FootballLeague, FootballTeam, FootballPlayer, CompetesIn, Competition
from .serializers import *


def home(request):
    context = {}
    return render(request, 'footballTeamsApp/home.html', context)

class FootballTeamList(generics.ListCreateAPIView):
    serializer_class = FootballTeamSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = {'yearOfFoundation': ['gte', 'lte']}

    ordering_fields = ['yearOfFoundation']


    def get_queryset(self):
        queryset = FootballTeam.objects.all()
        footballLeague = self.request.query_params.get('footballLeague') 
        if footballLeague is not None:
            queryset = queryset.filter(league = footballLeague)
        return queryset
    

class FootballTeamDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FootballTeamSerializer
    queryset = FootballTeam.objects.all()


class FootballLeagueList(generics.ListCreateAPIView):
    serializer_class = FootballLeagueSerializer
    queryset = FootballLeague.objects.all()


class FootballLeagueDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FootballLeagueSerializer
    queryset = FootballLeague.objects.all()


class FootballPlayerList(generics.ListCreateAPIView):
    serializer_class = FootballPlayerSerializer
    queryset = FootballPlayer.objects.all()


class FootballPlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FootballPlayerSerializer
    queryset = FootballPlayer.objects.all()


class CompetitionList(generics.ListCreateAPIView):
    serializer_class = CompetitionSerializer
    queryset = Competition.objects.all()


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompetitionSerializer
    queryset = Competition.objects.all()


class CompetesInList(generics.ListCreateAPIView):
    serializer_class = CompetesInSerializer
    queryset = CompetesIn.objects.all()


class CompetesInDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompetesInSerializer
    queryset = CompetesIn.objects.all()


class AverageAgeTeamsView(generics.ListAPIView):
    serializer_class = AverageAgeTeamsDTO

    def get_queryset(self):
        queryset = FootballTeam.objects.annotate(
            average_age = Avg('footballplayer__age'),
            team = F('teamName')
        ).exclude(average_age=None)
    
        ordering = self.request.query_params.get('ordering')
        if ordering == 'average_age':
            queryset = queryset.order_by('average_age')
        elif ordering == '-average_age':
            queryset = queryset.order_by('-average_age')

        return queryset.values('id', 'team', 'average_age')
    

class TeamsNumberOfPlayersView(generics.ListAPIView):
    serializer_class = TeamsNumberOfPlayersDTO

    def get_queryset(self):
        queryset = FootballTeam.objects.annotate(
            number_of_players = Count('footballplayer'),
            team = F('teamName')
        ).exclude(number_of_players=None)

        ordering = self.request.query_params.get('ordering')
        if ordering == 'number_of_players':
            queryset = queryset.order_by('number_of_players')
        elif ordering == '-number_of_players':
            queryset = queryset.order_by('-number_of_players')
            
        return queryset.values('id', 'team', 'number_of_players')