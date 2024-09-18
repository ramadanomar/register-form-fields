from django.dispatch import receiver
from django.db.models.signals import post_save
from openedx.core.djangoapps.user_api.models import UserProfile
from .models import ExtendedUserProfile


@receiver(post_save, sender=UserProfile)
def create_extended_user_profile(sender, instance, created, **kwargs):
    if created:
        ExtendedUserProfile.objects.create(user_profile=instance)
