from django.core.management import BaseCommand
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        os.remove("graph.json")

