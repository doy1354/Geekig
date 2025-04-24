"""Core > views > index.py"""
# PYTHON IMPORTS
import logging
from sys import _getframe
# DJANGO IMPORTS
from django.contrib import messages
from django.contrib.auth import get_user_model, views
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView
from django.contrib.auth.views import PasswordResetView
# CORE IMPORTS
from core.forms import SignupForm, LoginForm
from Accounting import settings
from .utlites import account_activation_token
from django.shortcuts import redirect


logger = logging.getLogger(__name__)
USER_MODEL = get_user_model()


# - LoginView, LogoutView used from django.contrib.auth.views
# - PasswordResetView sends the mail
# - PasswordResetDoneView shows a success message for the above
# - PasswordResetConfirmView checks clicked link and prompts for a new password
# - PasswordResetCompleteView shows a success message for the above


from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver

@receiver(user_logged_out)
def clear_session_data(sender, request, **kwargs):
    user = request.user
    user.save()


def redirect_auth_users(request, message=None):
    """Redirect authenticated users to index view"""
    logger.debug(  # prints function name and description
        f"{_getframe().f_code.co_name} "
        f"Redirecting {request.user} to IndexView..."
    )
    if not message:  # default message
        message = f"{request.user}, you are redirected to Index page."
    messages.info(request=request, message=message)
    return redirect(reverse_lazy('index'))


class SignupView(View):
    model = USER_MODEL
    form_class = SignupForm
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = SignupForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            current_site = get_current_site(request)
            email_subject = "Verify Your Email and Activate Your Geekig Account"
            message2 = render_to_string(
                'registration/email_confirmation.html',
                {
                    'name': f"{user.email}",
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user)
                }
            )
            user.verified_url = f"{current_site.domain}activate/{urlsafe_base64_encode(force_bytes(user.pk))}/account_activation_token.make_token(user)"
            user.save()
            email = EmailMultiAlternatives(
                email_subject,
                message2,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
            )
            email.attach_alternative(message2, "text/html")
            email.send()
            return redirect('email_verification')
            # return redirect('user_info')
        else:
            messages.error(request, form.errors)
            context = {
                'form': form
            }
            return render(request, self.template_name, context)


class LoginView(views.LoginView):
    """Overriding Django LoginView from django.contrib.auth.views"""

    form_class = LoginForm
    template_name = 'registration/login.html'

    @staticmethod
    def get_redirect_message(request):
        """Returns a message to user when redirected"""
        return f"Please logout if you wish to log in as a new user."

    def get(self, request, *args, **kwargs):
        """overriding GET method"""
        # create an instance of the login form
        form = self.form_class()

        # redirect authenticated users
        if request.user.is_authenticated:
            return redirect_auth_users(
                request=request, message=self.get_redirect_message(request)
            )

        # render the login template with the form
        return render(request, self.template_name, {'form': form})


class EmailVerification(TemplateView):

    """New user registration and signup view"""
    template_name = 'registration/user_verification.html'


class CustomPasswordResetView(PasswordResetView):
    def get_email_context(self):
        context = super().get_email_context()
        context['domain'] = 'localhost:8000'
        context['protocol'] = 'http'
        return context


class IndexView(TemplateView):
    """Index view"""
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        # redirect authenticated users
        print(request.user.is_authenticated, "*" * 20)
        if request.user.is_authenticated is False:
            return redirect('login')
        # render the index template
        return super().get(request, *args, **kwargs)
    
from django.core.mail import send_mail
from django.http import HttpResponse

def test_email_view(request):
    try:
        send_mail(
            subject='Password Reset Test',
            message='এইটা একটা টেস্ট ইমেইল। SMTP কাজ করছে কিনা চেক করার জন্য পাঠানো হয়েছে।',
            from_email='Accounting <rayhunkhan27@gmail.com>',
            recipient_list=['rayhunkhan27@gmail.com'],
            fail_silently=False,
        )
        return HttpResponse("✅ ইমেইল সফলভাবে পাঠানো হয়েছে।")
    except Exception as e:
        return HttpResponse(f"❌ ইমেইল পাঠাতে সমস্যা: {e}")
