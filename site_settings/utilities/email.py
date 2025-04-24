"""site_settings > utilities > email.py
"""
# PYTHON IMPORTS
from __future__ import absolute_import, unicode_literals
from sys import _getframe
import logging
# DJANGO IMPORTS
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


logger = logging.getLogger(__name__)


def send_email(email, template, **kwargs):
    """Sends an email with given template and returns status

    Valid parameters:
    email: str (or list)
    from_email: str (default: settings.DEFAULT_FROM_EMAIL)
    subject: str
    template: str
    context: str
    message: str (optional)
    """
    logger.debug(  # function name and message
        f"{_getframe().f_code.co_name} Sending email to: {email}"
    )
    # mail parameters
    params = kwargs.get('params', {})

    # to email
    if isinstance(email, str):
        email = [email, ]
    params.update({'recipient_list': email})

    # from email
    from_email = kwargs.get('from_email', settings.DEFAULT_FROM_EMAIL)
    params.update({'from_email': from_email})

    # process subject line
    subject = kwargs.get('subject', '')
    params.update({'subject': subject})

    # context
    context = kwargs.get('context', {})
    context.update({
        'protocol': 'https' if settings.ENABLE_HTTPS else 'http',
        'object': kwargs.get('object', None)
    })

    # email body or message
    message = kwargs.get('message', None)
    if not message:
        html_message = render_to_string(template, context)
        plain_message = strip_tags(html_message)
    else:
        html_message = None
        plain_message = message
    params.update({'message': plain_message, 'html_message': html_message})

    # send the email
    status = send_mail(**params)
    status = True if status > 0 else False

    state = 'sent' if status else 'failed'
    logger.debug(  # function name and message
        f"{_getframe().f_code.co_name} Email {state} with parameters: {params}"
    )
    return status
