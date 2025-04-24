"""Core > models > test_user.py"""
# PYTHON IMPORTS
import logging
from sys import _getframe
# DJANGO IMPORTS
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
# PROMETHEUS IMPORTS

logger = logging.getLogger(__name__)


class UserManager(BaseUserManager):
    """User Manager overridden from BaseUserManager for User"""

    def _create_user(self, email, password=None, **extra_fields):
        """Creates and returns a new user using an email address"""
        if not email:  # check for an empty email
            logger.error(  # prints class and function name
                f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
                f"User must set an email address"
            )
            raise AttributeError("User must set an email address")
        else:  # normalizes the provided email
            email = self.normalize_email(email)
            logger.debug(  # prints class and function name
                f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
                f"Normalized email: {email}"
            )

        # create user
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # hashes/encrypts password
        user.save(using=self._db)  # safe for multiple databases
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"User created: {user}"
        )
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Creates and returns a new user using an email address"""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Creating user: email={email}, extra_fields={extra_fields}"
        )
        return self._create_user(email, password, **extra_fields)

    def create_staffuser(self, email, password=None, **extra_fields):
        """Creates and returns a new staffuser using an email address"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Creating staffuser: email={email}, extra_fields={extra_fields}"
        )
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and returns a new superuser using an email address"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        logger.debug(  # prints class and function name
            f"{self.__class__.__name__}.{_getframe().f_code.co_name} "
            f"Creating superuser: email={email}, extra_fields={extra_fields}"
        )
        return self._create_user(email, password, **extra_fields)


class Activity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    """User model that supports using email instead of username"""
    requisitions = models.TextField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True,
                              blank=False, null=True
                              )
    # verified_url = models.CharField(max_length=255, null=True, blank=True)
    is_staff = models.BooleanField(default=False, null=True)
    is_accept = models.BooleanField(default=False)
    is_agree = models.BooleanField(default=False)
    is_info = models.BooleanField(default=False)
    is_tax_info = models.BooleanField(default=False)
    is_file = models.BooleanField(default=False)
    is_payment = models.BooleanField(default=False)
    is_bank = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, null=True
                                    )
    date_joined = models.DateTimeField(auto_now_add=True, null=True
                                       )
    last_updated = models.DateTimeField(auto_now=True, null=True
                                        )

    objects = UserManager()  # uses the custom manager

    USERNAME_FIELD = 'email'  # overrides username to email field

    def __str__(self):
        """User model string representation"""
        return self.email
