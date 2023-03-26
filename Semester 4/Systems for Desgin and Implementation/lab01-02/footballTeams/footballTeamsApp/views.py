from django.shortcuts import render
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import FootballLeague, FootballTeam
from .serializers import FootballLeagueSerializer, FootballTeamSerializer


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


# class FootballTeamFilter(generics.ListAPIView):
#     def get(self, request, year):
#         teams = FootballTeam.objects.filter(rating__gt = year)
#         serializer = FootballTeamSerializer(teams, many= True)
#         return response({"status": "success", "data" : serializer.data}, status = status.HTTP_2000)

