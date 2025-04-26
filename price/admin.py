from django.contrib import admin
from price import models


@admin.register(models.PricePlan)
class PricePlanAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'sub_title', 'price', 'credits', 'discount', 'is_active'
    )


@admin.register(models.Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('plan', 'price')


@admin.register(models.TransactionHistory)
class TransactionHistoryAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'plan')


@admin.register(models.RegionPaymentMethod)
class RegionPaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('region', 'payment_method')
