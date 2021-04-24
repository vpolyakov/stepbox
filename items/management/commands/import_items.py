from django.core.files.base import ContentFile
from django.core.management import BaseCommand

from items.models import Item
from utils.json import update_or_create_elements_from_json
from utils.request import request_content

ITEMS_URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/foodboxes.json'


def get_n_save_json_image(response, obj, element_id):
    """
    Сохраняет картинку в хранилище
    """
    image_content = response.content
    obj.image.save(f'food{element_id}.jpg', ContentFile(image_content))


def process_item(food_box, item):
    """
    Создает или обновляет item в БД, соответствующий Набору в json
    """
    item_tuple = item.objects.update_or_create(
        id=food_box['id'],
        defaults={
            'title': food_box['title'],
            'description': food_box['description'],
            'weight': food_box['weight_grams'],
            'price': float(food_box['price']),
        },
    )
    if item_tuple[1] and food_box['image']:
        # Если элемент удачно создан, и есть адрес откуда брать картинку, делает get запрос картинки
        request_content(food_box['image'], get_n_save_json_image, item_tuple[0], food_box["id"])


class Command(BaseCommand):
    def handle(self, *args, **options):
        request_content(ITEMS_URL, update_or_create_elements_from_json, process_item, Item)
