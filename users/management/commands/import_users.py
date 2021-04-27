from django.contrib.auth.hashers import make_password
from django.core.management import BaseCommand

from users.models import User
from utils.json import update_or_create_elements_from_json
from utils.request import request_content

USERS_URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/recipients.json'


def process_user(customer, user):
    user.objects.update_or_create(
        id=customer['id'],
        defaults={
            'email': customer['email'],
            'username': customer['email'].split("@")[0],
            'password': make_password(customer['password']),
            'first_name': customer['info']['name'],
            'last_name': customer['info']['surname'],
            'middle_name': customer['info']['patronymic'],
            'phone': customer['contacts']["phoneNumber"],
            'address': customer['city_kladr'],
        },
    )


class Command(BaseCommand):
    def handle(self, *args, **options):
        request_content(USERS_URL, update_or_create_elements_from_json, process_user, User)
