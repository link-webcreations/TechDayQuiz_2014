# -*- coding: utf-8 -*-

"""Quiz application model validators."""


from django.core.validators import ValidationError
from django.core.validators import RegexValidator


validate_letters_only = RegexValidator(regex='^(?u)([^\W\d_]|\s)+$',
                                       message='Only letters here.',
                                       code='invalid_lastname')


def validate_email_from_faurecia(email):
    """Validate that the user has typed a valid faurecia email."""
    if not email.lower().endswith('@faurecia.com'):
        raise ValidationError('Not a Faurecia email !')
