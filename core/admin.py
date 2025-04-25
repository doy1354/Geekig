"""Core > admin.py"""
# PYTHON IMPORTS
import logging
# DJANGO IMPORTS
from django.contrib import admin
from django.contrib.admin.models import LogEntry, DELETION
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.contenttypes.admin import GenericTabularInline
# PLUGIN IMPORTS
from import_export import resources
from import_export.admin import (
    ImportExportModelAdmin, ImportExportActionModelAdmin)
# PROJECT IMPORTS
from core import models

logger = logging.getLogger(__name__)


@admin.register(models.User)
class UserAdmin(
    ImportExportActionModelAdmin, ImportExportModelAdmin, UserAdmin
):
    """Admin for User model"""
    ordering = ('email', )
    list_display = (
        'email', 'is_superuser', 'is_active',
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
        ('Roles', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
        ('Dates', {'fields': ('last_login', 'last_updated', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': (
                'email', 'password1', 'password2'
            )
        }),
    )
    readonly_fields = ('last_login', 'last_updated', 'date_joined')
    search_fields = ('id', 'email')

    def get_inline_instances(self, request, obj=None):
        """hides inlines during 'add user' view"""
        return obj and super().get_inline_instances(request, obj) or []
