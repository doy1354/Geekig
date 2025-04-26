"""Core > urls.py"""
# DJANGO URLS
from django.urls import path
# CORE IMPORTS
from price import views

app_name = 'price'

urlpatterns = [
    # index url ---------------------------------------------------------------
    path('choice/plan/', views.ChoicePlan.as_view(), name='choice_plan'),
]
