# coding=utf-8
import warnings

from django.conf import settings
from django.db import models
from social_core.utils import setting_name

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

POSTGRES_JSONFIELD = getattr(settings, setting_name('POSTGRES_JSONFIELD'), False)

if POSTGRES_JSONFIELD:
    warnings.warn(
        'SOCIAL_AUTH_POSTGRES_JSONFIELD has been renamed to '
        'SOCIAL_AUTH_JSONFIELD_ENABLED and will be removed in the next release.'
    )
    JSONFIELD_ENABLED = True
else:
    JSONFIELD_ENABLED = getattr(settings, setting_name('JSONFIELD_ENABLED'), False)

if JSONFIELD_ENABLED:
    JSONFIELD_CUSTOM = getattr(settings, setting_name('JSONFIELD_CUSTOM'), None)
    if JSONFIELD_CUSTOM is not None:
        try:
            from django.utils.module_loading import import_string as import_module
        except ImportError:
            from importlib import import_module
        JSONField = import_module(JSONFIELD_CUSTOM)
    try:
        from django.db.models import JSONField
    except ImportError:
        from django.contrib.postgres.fields import JSONField
else:
    JSONField = models.TextField
