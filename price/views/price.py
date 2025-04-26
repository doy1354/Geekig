from django.shortcuts import render
from django.views.generic import View
from price.models import PricePlan
from django.contrib.auth.mixins import LoginRequiredMixin


class ChoicePlan(LoginRequiredMixin, View):

    """New user registration and signup view"""
    model = PricePlan
    template_name = 'price/choice_plan.html'

    def get(self, request, *args, **kwargs):
        """GET method for the view"""
        # Get the price plans from the database
        price_plans_in_china = PricePlan.objects.filter(
            is_active=True, inside_china=True
        ).order_by('price')
        price_plans_outside_china = PricePlan.objects.filter(
            is_active=True, inside_china=False
        ).order_by('price')
        context = {
            'price_plans_in_china': price_plans_in_china,
            'price_plans_outside_china': price_plans_outside_china,
        }

        return render(request, self.template_name, context=context)
