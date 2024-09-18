from django.db import models
from django.contrib.auth.models import User
from openedx.core.djangoapps.user_api.models import UserProfile


class ExtendedUserProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    work_phone_number = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.user_profile.user.username}'s extended profile"
