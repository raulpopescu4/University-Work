from django.contrib import admin
from .models import FootballLeague, FootballTeam, FootballPlayer, Competition, CompetesIn

admin.site.register(FootballLeague)
admin.site.register(FootballTeam)
admin.site.register(FootballPlayer)
admin.site.register(Competition)
admin.site.register(CompetesIn)