from django.db import models
from django.utils.timezone import now

# LOCAL IMPORT
from core.models import User, Activity

STATUS = (
    ('active', 'Active'),
    ('expire', 'Expire'),
    ('cancel', 'Cancel'),
    ('pending', 'Pending'),
)

MEETING_TYPE = (
    (1, "Without Payment"),
    (2, "With Payment"),
)


class MeetingLink(models.Model):
    type = models.PositiveIntegerField(unique=True, choices=MEETING_TYPE)
    link = models.URLField(verbose_name='link', blank=True, null=True)
    is_active = models.BooleanField(default=True)


class PricePlan(models.Model):
    DURATION_CHOICES = (
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    )

    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=1500, null=True, blank=True)
    price = models.IntegerField()
    api_keys = models.CharField(max_length=255, null=True)
    plan_img = models.ImageField(
        upload_to='Plan Images', blank=True, verbose_name='Plan Images')
    is_free = models.BooleanField(default=False)
    duration = models.CharField(max_length=10, choices=DURATION_CHOICES)
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, null=True, blank=True
    )
    appointment_point = models.PositiveIntegerField(default=0)

    # Add a unique constraint to enforce uniqueness of title and duration together
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'duration', 'activity'], name='unique_title_duration')
        ]

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    plan = models.ForeignKey(PricePlan, on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=50, null=True)
    payment_method = models.CharField(max_length=50, null=True, blank=True)
    subscription_from = models.DateField(
        verbose_name='Subscription From', null=True)
    subscription_to = models.DateField(
        verbose_name='Subscription To', null=True)
    stripeCustomerId = models.CharField(
        max_length=255, verbose_name='Stripe Customer Id',
        null=True, blank=True)
    stripeSubscriptionId = models.CharField(
        max_length=255, verbose_name='Stripe Subscription Id',
        null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=50, null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Updated At')

    class Meta:
        verbose_name_plural = 'Subscribers'


class TransactionHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(PricePlan, on_delete=models.CASCADE, null=True)
    inserted_on = models.DateField(default=now, null=True, blank=True)
    updated_on = models.DateField(default=now, null=True, blank=True)

    def __str__(self):
        return self.plan.title
