"""Core > urls.py"""
# DJANGO URLS
from django.urls import path
# CORE IMPORTS
from price import views

app_name = 'price'

urlpatterns = [
    # index url ---------------------------------------------------------------
    path('card/', views.UserCard.as_view(), name='user_card'),
    path('free/plan/<int:pk>/', views.FreePlan.as_view(), name='free_plan'),
    path('cancel/subscription', views.CancelSubscription.as_view(),name='cancel_subscription'),
    path('checkout/<int:plan>/', views.Checkout.as_view(),name='checkout'),
    path('checkout/session/<int:plan>/', views.CheckoutSession.as_view(),name='checkout_session'),
    path('payment/success', views.PaymentSuccess.as_view(), name='payment_success'),
]
