from datetime import datetime

from django.core.management import BaseCommand

from reviews.models import Reviews
from utils.json import update_or_create_elements_from_json
from utils.request import request_content

REVIEW_URL = 'https://raw.githubusercontent.com/stepik-a-w/drf-project-boxes/master/reviews.json'


def assign_status(request_review, reviews):
    status = None
    if request_review['status'] == 'published':
        status = reviews.PUBLISHED
    elif request_review['status'] == 'hidden':
        status = reviews.REJECTED
    elif request_review['status'] == 'new':
        status = reviews.ON_MODERATION
    return status


def process_review(request_review, reviews):
    status = assign_status(request_review, reviews)

    if status:
        published_at = (
            datetime.strptime(request_review['published_at'], '%Y-%m-%d') if request_review['published_at'] else None
        )
        reviews.objects.update_or_create(
            id=request_review['id'],
            defaults={
                "author_id": request_review['author'],
                "text": request_review["content"],
                "created_at": datetime.strptime(request_review["created_at"], '%Y-%m-%d'),
                "published_at": published_at,
                "status": status,
            },
        )


class Command(BaseCommand):
    def handle(self, *args, **options):
        request_content(REVIEW_URL, update_or_create_elements_from_json, process_review, Reviews)
