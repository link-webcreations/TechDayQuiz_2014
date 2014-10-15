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
        self.site = self.site.upper()
        super(Participant, self).save(*args, **kwargs)

    def show_results(self, quiz_id=None):
        if not quiz_id:
            raise TypeError('Provides quiz_id !')

        results = {
            'quiz': Quiz.objects.get(id=quiz_id).name,
            'good': [],
            'bad': [],
            'num_good': 0,
            'num_bad': 0,
            'total': 0,
        }

        for given in self.given_answers.filter(answer__question__quiz=quiz_id):
            if given.answer.is_correct:
                results['good'].append(given.answer.question.content)
            else:
                results['bad'].append(given.answer.question.content)

        # Count good/bad responses
        results['num_good'] = len(results['good'])
        results['num_bad'] = len(results['bad'])
        results['total'] = Question.objects.filter(quiz__id=quiz_id).count()

        return results

    @property
    def fullname(self):
        return u"{0.firstname} {0.lastname}".format(self)

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
    author = models.ForeignKey(User,
                               blank=True,
                               editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"{0.name}".format(self)


class Question(models.Model):
    """
    Base class for creating a quiz's question.
    """
    quiz = models.ForeignKey('Quiz', related_name='questions')
    content = models.CharField(max_length=1024)

    def __unicode__(self):
        return u"{0.content}".format(self)


class FreeQuestion(Question):
    """
    A quiz's question with a free answer.
    """
    answer_must_match = models.CharField(
        max_length=1024,
        help_text='The good answer that the participant must provides.'
    )


class ChoiceQuestion(Question):
    """
    A quiz's question with answer proposals.
    """
    pass


class Answer(models.Model):
    """
    A question answer.

    Participant must choice only one for a question.
    """
    question = models.ForeignKey('Question', related_name='answers')
    content = models.CharField(max_length=1024, blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    def __unicode__(self):
        return u"{0.content} ({0.is_correct})".format(self)


class ParticipantAnswer(models.Model):
    """A participant answer."""
    class Meta:
        unique_together = (('participant', 'question'),)

    participant = models.ForeignKey(
        'Participant', related_name="given_answers")
    question = models.ForeignKey(
        'Question', related_name="given_answers")
    answer = models.ForeignKey(
        'Answer', blank=True, null=True)
    content = models.CharField(
        max_length=1024, blank=True, null=True)

    def __unicode__(self):
        participant = u"{0.firstname} {0.lastname}".format(self.participant)
        if not self.answer:
            return u"{0}: {1.content}".format(participant, self)
        else:
            return u"{0}: {1.answer}".format(participant, self)
