"""site_settings > models > abstract.py"""
# DJANGO IMPORTS
import logging
from django.db import models
from django.conf import settings
from django.utils import timezone

logger = logging.getLogger(__name__)


class AbstractBaseFields(models.Model):
    is_active = models.BooleanField(default=True
    )
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_created"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True
    )

    updated_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_updated"
    )
    last_updated = models.DateTimeField(auto_now=True, null=True
    )

    is_deleted = models.BooleanField(default=False
    )
    deleted_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_deleted"
    )
    deleted_at = models.DateTimeField(blank=True, null=True
    )

    def soft_delete(self):
        self.is_deleted = True
        self.is_active = False
        self.deleted_at = timezone.now()
        self.save()

    def soft_deactivate(self):
        self.is_active = False
        self.save()

    class Meta:
        abstract = True
