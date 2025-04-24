"""Core > models > profile.py"""
# PYTHON IMPORTS
import logging
from sys import _getframe
# DJANGO IMPORTS
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
# CORE IMPORTS
from core.models import User
# PROMETHEUS IMPORTS


logger = logging.getLogger(__name__)


def media_upload_path(instance, filename):
    """Returns formatted upload to path"""
    path = f'Users/{instance.user.id}/{filename}'
    logger.debug(  # prints class and function name
        f"{_getframe().f_code.co_name} Media upload path: {path}"
    )
    return path


class Profile(models.Model):
    """User Profile model"""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, unique=True
    )
    image = models.ImageField(blank=True, null=True,
                              upload_to=media_upload_path)

    def __str__(self):
        """String representation of Profile model"""
        return self.user.email


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """Creates or updates profile, when User object changes"""
    if created:
        logger.debug(  # prints class and function name
            f"{_getframe().f_code.co_name} Creating {instance}'s profile"
        )
        Profile.objects.get_or_create(user=instance)
    logger.debug(  # prints class and function name
        f"{_getframe().f_code.co_name} Saving {instance}'s profile"
    )
    instance.profile.save()
