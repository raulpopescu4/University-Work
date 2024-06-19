from rest_framework import serializers
from .models import FootballLeague, FootballTeam, FootballPlayer, Competition, CompetesIn

class FootballTeamSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if len(data['yearOfFoundation']) != 4:
            raise serializers.ValidationError('The team\' year of foundation must be of 4 digits long')
        
        return data
    
    class Meta:
        model = FootballTeam
        fields = ('__all__')


class FootballLeagueSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not data['yearOfFoundation'].isdigit():
            raise serializers.ValidationError('The league\' year of foundation must be an integer')
        
        return data
    
    class Meta:
        model = FootballLeague
        fields = ('__all__')


class FootballPlayerSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if not data['age'].isdigit():
            raise serializers.ValidationError('The player\'s age must contain only digits')

        if len(data['height']) != 3:
            raise serializers.ValidationError('The player\'s height must be of 3 digits long')
        
        return data
    
    class Meta:
        model = FootballPlayer
        fields = ('__all__')


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ('__all__')


class CompetesInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetesIn
        fields = ('__all__')


class AverageAgeTeamsDTO(serializers.Serializer):
    id = serializers.IntegerField()
    team = serializers.CharField()
    average_age = serializers.FloatField()


class TeamsNumberOfPlayersDTO(serializers.Serializer):
    id = serializers.IntegerField()
    team = serializers.CharField()
    number_of_players = serializers.IntegerField()

 