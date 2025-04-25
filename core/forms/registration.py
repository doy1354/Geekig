"""Core > forms > registration.py"""
# DJANGO IMPORTS
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

USER_MODEL = get_user_model()


class SignupForm(UserCreationForm):
    """New user registration and signup form"""

    class Meta:
        """Meta class"""
        model = USER_MODEL
        fields = ('email', 'is_accept')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.pop('autofocus', False)


class LoginForm(UserCreationForm):
    """Login form for user authentication"""

    class Meta:
        """Meta class"""
        model = USER_MODEL
        fields = ('email', 'password')
