# Generated by Django 3.2 on 2025-04-26 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0003_priceplan_inside_china'),
    ]

    operations = [
        migrations.AddField(
            model_name='priceplan',
            name='is_discount',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='priceplan',
            name='api_keys',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
