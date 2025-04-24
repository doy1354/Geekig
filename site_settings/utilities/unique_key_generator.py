"""site_settings > utilities > unique_key_generator.py"""
# PYTHON IMPORTS
import uuid
from datetime import datetime


def unique_key_generator():
    timestamp = datetime.timestamp(datetime.now())
    uuid_key = uuid.uuid4()
    key = f"{uuid_key}-{timestamp}"
    return key
