import stripe
import datetime
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.decorators.csrf import ensure_csrf_cookie
from Accounting import settings
from price.models import PricePlan, Subscriber, TransactionHistory
from django.contrib.auth.mixins import LoginRequiredMixin


class FreePlan(LoginRequiredMixin, View):
    """Free plan view"""
    def get(self, request, pk, *args, **kwargs):
        plan = PricePlan.objects.get(pk=pk)
        subscriber = Subscriber.objects.filter(user=request.user, status='active')
        for price in subscriber:
            pass

        subscription = Subscriber.objects.create(
            plan=plan, user=request.user, price=plan.price, status='active',
            payment_method='free', subscription_from=datetime.date.today(),
        )
        return redirect('index')


class UserCard(LoginRequiredMixin, View):

    """New user registration and signup view"""
    model = PricePlan
    template_name = 'price/pricing_plan.html'

    def get(self, request, *args, **kwargs):
        user = request.user

        monthly_plans = PricePlan.objects.filter(
            Q(is_free=True) | Q(duration='monthly')
        )
        yearly_plans = PricePlan.objects.filter(
            duration='yearly'
        )

        sub_exist=''
        if not Subscriber.objects.filter(user=request.user, status='active', plan__is_free=False).exists():
            sub_exist='No'
            subscriber=None
        else:
            sub_exist='Yes'

            subscriber = Subscriber.objects.get(user=request.user, status='active')
            stripe.api_key = settings.STRIPE_SECRET_KEY
            retrieve_sub = stripe.Subscription.retrieve(
                subscriber.stripeSubscriptionId
            )
            if retrieve_sub.status == "active":
                subscriber.status = 'active'
                subscriber.save()
            else:
                subscriber.status = 'cancel'
                subscriber.save()
        context = {
            'monthly_plans': monthly_plans, 'sub_exist':sub_exist,
            'yearly_plans': yearly_plans,
            'current_active_plan':subscriber
        }
        return render(request, self.template_name, context)


class CancelSubscription(LoginRequiredMixin, View):
    """Cancel subscription view"""
    def get(self, request, *args, **kwargs):
        subscriber=Subscriber.objects.get(user=request.user, status='active')
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.Subscription.delete(
            subscriber.stripeSubscriptionId
        )
        subscriber.status='Cancel'
        subscriber.save()
        messages.error(request,'Active subscription cancelled successfully.')
        return redirect('price:user_card')


class Checkout(LoginRequiredMixin, View):
    """Cancel subscription view"""
    def get(self, request, plan, *args, **kwargs):
        planDetail = PricePlan.objects.get(pk=plan)
        if not Subscriber.objects.filter(user=request.user, status='active').exists():
            return render(request, 'price/checkout.html', {'plan': planDetail})
        else:
            error_message_text='You already have subscription of this ' + planDetail.title + ' plan.'
            messages.error(request,error_message_text )

            return redirect('price:user_card')


class CheckoutSession(LoginRequiredMixin, View):
    """Cancel subscription view"""
    def get(self, request, plan, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        plan = PricePlan.objects.get(pk=plan)
        plan_price = plan.api_keys

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                "price": plan_price,
                'quantity': 1,
            }],

            mode='subscription',
            success_url=f'{request.build_absolute_uri("/")}'+'price/payment/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=f'{request.build_absolute_uri("/")}'+'price/payment/cancel',

            client_reference_id=plan.pk

        )
        return redirect(session.url, code=303)


class PaymentSuccess(LoginRequiredMixin, View):
    """Cancel subscription view"""
    def get(self, request, *args, **kwargs):
        # try:
        user_bank_id = request.session.get('user_bank_id')
        session_id = request.GET.get("session_id")
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.retrieve(session_id)
        plan_id = session.client_reference_id
        stripe_subscription_id = session.subscription
        stripe_customer_id = session.customer
        plan = PricePlan.objects.get(pk=plan_id)

        user = request.user
        user.appointment_point = plan.appointment_point
        user.save()
        try:
            subscriber_details = Subscriber.objects.get(user=user, status='active')
            subscriber_details.status = 'expire'
            subscriber_details.save()
        except Exception as e:
            pass

        subscription_from = datetime.date.today()
        subscription_to = datetime.date.today() + relativedelta(months=1)

        subscription = Subscriber.objects.create(
            plan=plan, user=user, price=plan.price, status='active',
            payment_method='Stripe', subscription_from=subscription_from,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_subscription_id,
            subscription_to=subscription_to
        )
        request.session['subscription'] = subscription.pk
        #creating a transaction
        TransactionHistory.objects.create(user_id=user, plan=plan)
        return redirect("get_user_bank", pk=request.user.pk)