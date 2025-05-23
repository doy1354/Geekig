# Generated by Django 3.2 on 2025-04-23 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import site_settings.models.settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('domain', models.CharField(max_length=100, validators=[site_settings.models.settings._simple_domain_name_validator])),
                ('name', models.CharField(max_length=255)),
                ('short_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', models.FileField(blank=True, help_text='Logo on the navbar', null=True, upload_to='logo/%Y/%m/%d/')),
                ('favicon', models.FileField(blank=True, help_text='Favicon on the meta title', null=True, upload_to='favicon/%Y/%m/%d/')),
                ('bg_color', models.CharField(blank=True, max_length=100, null=True)),
                ('text_color', models.CharField(blank=True, max_length=100, null=True)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='site_settings_sitesettings_created', to=settings.AUTH_USER_MODEL)),
                ('deleted_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='site_settings_sitesettings_deleted', to=settings.AUTH_USER_MODEL)),
                ('updated_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='site_settings_sitesettings_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Site Settings',
                'verbose_name_plural': 'Site Settings',
                'unique_together': {('domain', 'is_active')},
            },
        ),
    ]
