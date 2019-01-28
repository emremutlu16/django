from django.core.management import BaseCommand
from django.contrib.auth.models import User
from api.models import UserLogin


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        if options['username']:
            try:
                user = User.objects.get(username=options['username'])
                UserLogin.objects.save_token(user)
            except Exception as e:
                raise Exception("Error: ", e)
