from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Limpa os dados existentes
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Cria times
        marvel = Team.objects.create(name='marvel', description='Time Marvel')
        dc = Team.objects.create(name='dc', description='Time DC')

        # Cria usuários
        tony = User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel.name)
        steve = User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel.name)
        bruce = User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc.name)
        diana = User.objects.create(email='diana@themyscira.com', name='Diana Prince', team=dc.name)

        # Cria atividades
        Activity.objects.create(user=tony, type='corrida', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='natação', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='ciclismo', duration=60, date=timezone.now().date())
        Activity.objects.create(user=diana, type='corrida', duration=50, date=timezone.now().date())

        # Cria treinos
        w1 = Workout.objects.create(name='Supino', description='Supino reto', difficulty='médio')
        w2 = Workout.objects.create(name='Agachamento', description='Agachamento livre', difficulty='difícil')

        # Cria leaderboard
        Leaderboard.objects.create(user=tony, score=120, rank=1)
        Leaderboard.objects.create(user=steve, score=110, rank=2)
        Leaderboard.objects.create(user=bruce, score=100, rank=3)
        Leaderboard.objects.create(user=diana, score=90, rank=4)

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de teste!'))
