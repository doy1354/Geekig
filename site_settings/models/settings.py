"""site_settings > models > settings.py"""
# DJANGO IMPORTS
import string
from django.db import models
from django.core.exceptions import ValidationError
# APP IMPORTS
from site_settings.models import AbstractBaseFields


def _simple_domain_name_validator(value):
    """
    Validate that the given value contains no whitespaces to prevent common
    typos.
    """
    checks = ((s in value) for s in string.whitespace)
    if any(checks):
        raise ValidationError(
            _("The domain name cannot contain any spaces or tabs."),
            code='invalid',
        )


class SiteSettings(AbstractBaseFields):
    domain = models.CharField(
        max_length=100,
        validators=[_simple_domain_name_validator]
    )
    name = models.CharField(max_length=255
    )
    short_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.FileField(
        upload_to="logo/%Y/%m/%d/",
        blank=True, null=True,
        help_text="Logo on the navbar",
    )
    favicon = models.FileField(
        upload_to="favicon/%Y/%m/%d/",
        blank=True, null=True,
        help_text="Favicon on the meta title"
    )
    bg_color = models.CharField(max_length=100,
        blank=True, null=True
    )
    text_color = models.CharField(max_length=100,
        blank=True, null=True
    )

    class Meta:
        unique_together = ('domain', 'is_active')
        verbose_name_plural = "Site Settings"
        verbose_name = "Site Settings"

    def __str__(self):
        return self.name
