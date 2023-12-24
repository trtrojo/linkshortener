from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import UrlSequence

@receiver(post_migrate)
def create_default_sequence(sender, **kwargs):
    UrlSequence.objects.get_or_create(defaults={'current_value': 0})
