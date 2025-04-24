"""site_settings > models > __init__.py"""
# APP IMPORTS
from .abstract import AbstractBaseFields
from .settings import SiteSettings

__all__ = [
    AbstractBaseFields,
    SiteSettings,
]
