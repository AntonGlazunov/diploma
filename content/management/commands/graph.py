from django.core.management import BaseCommand

from config.settings import GRAPH
from content.models import Movie
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        films = Movie.objects.all()
        users = User.objects.all()
        for film in films:
            GRAPH.add_node(film.name)
        for user in users:
            GRAPH.add_node(user.pk)
