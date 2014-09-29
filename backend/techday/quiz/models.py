# -*- coding: utf-8 -*-

"""Quiz application models definitions."""

from django.db import models

from .validators import (
    validate_letters_only,
    validate_email_from_faurecia,
)


class Person(models.Model):
    firstname = models.CharField(max_length=255,
                                 validators=[validate_letters_only])
    lastname = models.CharField(max_length=255,
                                validators=[validate_letters_only])
    email = models.EmailField(max_length=254,
                              validators=[validate_email_from_faurecia],
                              unique=True)

    def save(self, *args, **kwargs):
        """Customize saving of model."""
        self.firstname = self.firstname.title()
        self.lastname = self.lastname.upper()
        self.email = self.email.lower()
        super(Person, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"{0.firstname} {0.lastname} <{0.email}>".format(self)
