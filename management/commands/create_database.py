from django.core.management.base import BaseCommand
from app.models import Question, Tag, LikeToQue, LikeToAns, Profile, Answer


class Create(BaseCommand):

    def create_data(self):
        tag_to_create = [Tag(tag_title=f"Title #{i}", rating=i) for i in range(12000)]
        Tag.objects.bulk_create(tag_to_create)
