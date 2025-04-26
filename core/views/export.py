"""Core > views > index.py"""
from django.views.generic import TemplateView


class ExportView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any additional context data here if needed
        return context
