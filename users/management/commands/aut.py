from django.core.management import BaseCommand

from config.settings import GRAPH
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='tagl91@yandex.ru',
        )
        user.set_password('200818fynjirf')
        user.save()

        user = User.objects.create(
            email='test@mail.com',
        )
        user.set_password('200818')
        user.save()

        user = User.objects.create(
            email='test1@mail.com',
        )
        user.set_password('200818')
        user.save()

        user = User.objects.create(
            email='test2@mail.com',
        )
        user.set_password('200818')
        user.save()

        user = User.objects.create(
            email='test3@mail.com',
        )
        user.set_password('200818')
        user.save()

        user = User.objects.create(
            email='test4@mail.com',
        )
        user.set_password('200818')
        user.save()

        user = User.objects.create(
            email='test5@mail.com',
        )
        user.set_password('200818')
        user.save()
