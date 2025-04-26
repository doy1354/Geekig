from django.db import models

# LOCAL IMPORT
from core.models import User


REGION_CHOICES = (
    ('inside_china', 'Inside China'),
    ('outside_china', 'Outside China'),
)


class PricePlan(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=1500, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    api_keys = models.CharField(max_length=255, null=True, blank=True)
    credits = models.PositiveIntegerField(default=0)
    is_discount = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Updated At')
    is_active = models.BooleanField(default=True)
    inside_china = models.BooleanField(default=True)
    is_popular = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Price Plans'

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    plan = models.ForeignKey(PricePlan, on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=50, null=True)
    payment_method = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Updated At')

    class Meta:
        verbose_name_plural = 'Subscribers'


class TransactionHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(PricePlan, on_delete=models.CASCADE, null=True)
    credits = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.plan.title


class RegionPaymentMethod(models.Model):

    PAYMENT_METHODS_INSIDE_CHINA = (
        ('ali_pay', 'Ali Pay'),
        ('wechat_pay', 'WeChat Pay'),
        ('usdt', 'USDT'),
    )

    PAYMENT_METHODS_OUTSIDE_CHINA = (
        ('google_pay', 'Google Pay'),
        ('stripe', 'Stripe'),
        ('paypal', 'PayPal'),
    )

    region = models.CharField(
        max_length=20, choices=REGION_CHOICES, verbose_name='Region')
    payment_method = models.CharField(
        max_length=20, verbose_name='Payment Method')

    def __str__(self):
        return f"{self.get_region_display()} - {self.get_payment_method_display()}" # noqa
