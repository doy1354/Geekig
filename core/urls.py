"""Core > urls.py"""
# DJANGO URLS
from django.urls import path
from core.views import ExportView
# CORE IMPORTS
app_name = 'core'

urlpatterns = [
    path('export/', ExportView.as_view(), name='export'),
]
