"""Core > urls.py"""
# DJANGO URLS
from django.urls import path
# CORE IMPORTS
from price import views

app_name = 'price'

urlpatterns = [
    # index url ---------------------------------------------------------------
    path('card/', views.UserCard.as_view(), name='user_card'),
]
