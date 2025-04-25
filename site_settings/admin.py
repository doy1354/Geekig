"""site_settings > models > admin.py"""
# DJANGO IMPORTS
from django.contrib import admin
# APP IMPORTS
from site_settings import models


@admin.register(models.SiteSettings)
class SiteSettingsModelAdmin(admin.ModelAdmin):
    list_display = [
        'domain', 'name', 'short_name',
        'created_user', 'updated_user', 'is_active'
    ]
    search_fields = ['domain', 'name', 'short_name']
    readonly_fields = ('created_at', 'last_updated')
    list_filter = ['is_active']

    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_user = request.user
        else:
            obj.created_user = request.user
        super().save_model(request, obj, form, change)
