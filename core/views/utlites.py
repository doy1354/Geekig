from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.shortcuts import redirect
from core.models import User
from django.http import JsonResponse
from django.utils import six
from django.contrib.auth import login
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()


def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user, backend=backend)
        # return redirect('price:user_card')
        return redirect('/')
    elif user.is_active:
        return redirect('/')
    else:
        return redirect('signup')


def update_session_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            # Update session with the selected language
            request.session['django_language'] = language
            return redirect(request.POST.get('next') or 'index')
    return redirect('index')
