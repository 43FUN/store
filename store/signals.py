from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from store.models import Wallet


@receiver(post_save, sender=User)
def create_wallet(instance, sender, **kwargs):
    Wallet.objects.get_or_create(user=instance)
