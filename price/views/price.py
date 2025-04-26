from django.shortcuts import render
from django.views.generic import View
from price.models import PricePlan
from django.contrib.auth.mixins import LoginRequiredMixin


class ChoicePlan(LoginRequiredMixin, View):

    """New user registration and signup view"""
    model = PricePlan
    template_name = 'price/choice_plan.html'

    def get(self, request, *args, **kwargs):
        pass

        return render(request, self.template_name)
