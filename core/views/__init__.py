"""Core > views > __init__.py"""
from .registration import (
    SignupView, LoginView, EmailVerification, IndexView,
    CustomPasswordResetView
)
from .utlites import activate, update_session_language
from .export import ExportView


# update the following list to allow classes to be available for import
# this is very useful especially when using from .file import *
__all__ = [
    SignupView, LoginView, EmailVerification, IndexView, activate,
    update_session_language, CustomPasswordResetView, ExportView
]
