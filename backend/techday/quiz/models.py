# -*- coding: utf-8 -*-

"""Quiz application models definitions."""

from django.db import models
from django.contrib.auth.models import User

from .validators import (
    validate_letters_only,
    validate_email_from_faurecia,
)


class Participant(models.Model):
    """
    A participant who submit a quiz result.
    """
    firstname = models.CharField(max_length=255,
                                 validators=[validate_letters_only])
    lastname = models.CharField(max_length=255,
                                validators=[validate_letters_only])
    email = models.EmailField(max_length=254,
                              validators=[validate_email_from_faurecia],
                              unique=True)
    site = models.CharField(max_length=255,
                            validators=[validate_letters_only])

    def save(self, *args, **kwargs):
        """Customize saving of model."""
        self.firstname = self.firstname.title()
        self.lastname = self.lastname.upper()
        self.email = self.email.lower()
        self.site = self.email.upper()
        super(Participant, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"{0.firstname} {0.lastname} <{0.email}>".format(self)


class Quiz(models.Model):
    """
    Creates a new Quiz.

    A quiz contains one or more questions.
    """
    class Meta:
        verbose_name_plural = "Quizzes"

    name = models.CharField(max_length=255)
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"{0.name}".format(self)


class Question(models.Model):
    """
    A quiz's question.
    """
    quiz = models.ForeignKey('Quiz', related_name='questions')
    content = models.CharField(max_length=1024)

    def __unicode__(self):
        return u"{0.content}".format(self)


class Answer(models.Model):
    """
    A question answer.
    """
    question = models.ForeignKey('Question', related_name='answers')
    content = models.CharField(max_length=1024)
    is_correct = models.BooleanField(default=False)

    def __unicode__(self):
        return u"{0.content} ({0.is_correct})".format(self)
