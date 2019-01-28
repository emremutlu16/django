from django.core.management.base import BaseCommand, CommandError
from api.models import RandomUser
import requests


class Command(BaseCommand):
    help = 'Get Random User'

    # def add_arguments(self, parser):
    #     parser.add_argument('randomuser', nargs='+', type=int, help='name')
    # while

    def handle(self, *args, **options):
        url = 'https://randomuser.me/api/?results=5000'
        response = requests.get(url)
        users = response.json().get("results")
        bulk_list = []

        for user in users:
            obj = RandomUser(
                name=user['name']['first'],
                last_name=user['name']['last'],
                mobile_number=user['phone'],
                age=user['dob']['age']
            )
            bulk_list.append(obj)
        RandomUser.user_obj.save_data(bulk_list)
