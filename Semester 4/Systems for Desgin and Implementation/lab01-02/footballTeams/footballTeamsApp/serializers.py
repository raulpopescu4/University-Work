from rest_framework import serializers
from .models import FootballLeague, FootballTeam

class FootballTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballTeam
        fields = ('__all__')


class FootballLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballLeague
        fields = ('__all__')