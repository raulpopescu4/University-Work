from django.db import models


class FootballLeague(models.Model):
    leagueName = models.CharField(max_length= 100, unique= True)
    yearOfFoundation = models.SmallIntegerField()
    domesticCup = models.CharField(max_length= 100)
    numberOfTeams = models.SmallIntegerField(null = True)
    confederation = models.CharField(max_length= 50, null = True)

    def __str__(self):
        return self.leagueName


class FootballTeam(models.Model):
    teamName = models.CharField(max_length= 100, unique=True)
    yearOfFoundation = models.SmallIntegerField()
    ground = models.CharField(max_length = 50)
    presidentName = models.CharField(max_length= 100)
    league = models.ForeignKey(FootballLeague, default= None, blank= True, null= True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.teamName
    

class FootballPlayer(models.Model):
    name = models.CharField(max_length= 100)
    age = models.SmallIntegerField()
    height = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    team = models.ForeignKey(FootballTeam, default= None, null= True, blank= True, on_delete= models.SET_NULL)
    

