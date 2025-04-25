"""Core > forms > user.py"""
# DJANGO IMPORTS
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.forms.widgets import ClearableFileInput
# CORE IMPORTS
from core.models import User


class CustomClearableFileInput(ClearableFileInput):
    template_name = 'templates/custom_clearable_file_input.html' 


class ChangePasswordForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

    def clean_new_password2(self):
        # Add custom validation if needed
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("New passwords must match.")
        return new_password2
