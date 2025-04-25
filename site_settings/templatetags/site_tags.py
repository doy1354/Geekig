"""site_settings > templatetags > site_tags.py"""
# PYTHON IMPORTS
import logging
# DJANGO IMPORTS
from django import template
# APP IMPORTS
from site_settings.utilities import en_to_bn_number_converter

register = template.Library()

logger = logging.getLogger(__name__)


@register.filter
def en_to_bn_num_converter(values):
    return en_to_bn_number_converter(values)


@register.filter
def in_list(value, the_list):
    value = str(value)
    return value in the_list
