from django.urls import reverse
from rest_framework.test import APITestCase

from footballTeamsApp.models import *

class ViewsTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_teams = 10
        for team_id in range(number_of_teams):
            FootballTeam.objects.create(teamName = f'team{team_id}', yearOfFoundation = team_id, ground= f'{team_id}', presidentName= f'{team_id}')

        number_of_players = 7

        for player_id in range(number_of_players):
            FootballPlayer.objects.create(name = f'player{player_id}', age= 10, height = player_id, weight= player_id, team = FootballTeam.objects.first())


    def test_average_age_teams_view_url_exists(self):
        response = self.client.get('/avg_age_statistics/')
        self.assertEqual(response.status_code, 200)

    def test_average_age_teams(self):
        respone = self.client.get('/avg_age_statistics/')

        self.assertEqual(len(respone.data), 1)


    def test_teams_number_of_players_view_url_exists(self):
        response = self.client.get('/teams_by_number_of_players/')
        self.assertEqual(response.status_code, 200)

    
    def test_average_age_teams(self):
        respone = self.client.get('/teams_by_number_of_players/')

        self.assertEqual(len(respone.data), 10)
