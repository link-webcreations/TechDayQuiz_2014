# -*- coding: utf-8 -*-

"""Quiz application models definitions."""

from django.db import models

from .validators import (
    validate_letters_only,
    validate_email_from_faurecia,
)


class Person(models.Model):
    """A person who submit a quiz result."""
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


class Quiz(models.Model):
    """
    Creates a new Quiz.

    A quiz contains one or more questions.
    """
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u"{0.name}".format(self)


class Question(models.Model):
    """
    A quiz's question.

    A question that is part of an unique quiz.
    A question has a right answer to validate it.
    """
    quiz = models.ForeignKey('Quiz')
    ask = models.CharField(max_length=1024)
    right_answer = models.CharField(max_length=1024)

    def __unicode__(self):
        return u"{0.ask} ({0.right_answer})".format(self)


class Answer(models.Model):
    """
    Answer given for a question by a person.
    """
    person = models.ForeignKey('Person')
    question = models.ForeignKey('Question')
    value = models.CharField(max_length=1024)

    def __unicode__(self):
        return u"{0.person.email}: {0.value}".format(self)
