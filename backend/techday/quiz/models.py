# -*- coding: utf-8 -*-

"""Quiz application models definitions."""

from difflib import SequenceMatcher

from django.db import models
from django.contrib.auth.models import User

from .validators import validate_email_from_faurecia


class Participant(models.Model):
    """
    A participant who submit a quiz result.
    """
    firstname = models.CharField(max_length=255,
                                 blank=True,
                                 null=True)
    lastname = models.CharField(max_length=255,
                                blank=True,
                                null=True)
    email = models.EmailField(max_length=254,
                              validators=[validate_email_from_faurecia],
                              unique=True)

    def save(self, *args, **kwargs):
        """Customize saving of model."""
        email = self.email.lower()
        firstname, lastname = email.split('@')[0].split('.')

        self.firstname = firstname.title()
        self.lastname = lastname.upper()
        self.email = email
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

        for given in self.given_answers.filter(question__quiz=quiz_id):
            # For questions with choices
            if hasattr(given.question, 'choicequestion'):
                if given.answer.is_correct:
                    results['good'].append(given.answer.question.content)
                else:
                    results['bad'].append(given.answer.question.content)
            # For questions with free answer
            elif hasattr(given.question, 'freequestion'):
                response = given.question.freequestion.answer_must_match
                if given.content.isnumeric() and response.isnumeric():
                    content = int(given.content)
                    response = int(response)
                    if content == response:
                        results['good'].append(given.question.content)
                    else:
                        results['bad'].append(given.question.content)
                else:
                    matcher = SequenceMatcher(None,
                                              given.content.lower(),
                                              response.lower())
                    if matcher.ratio() > 0.90:
                        results['good'].append(given.question.content)
                    else:
                        results['bad'].append(given.question.content)

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
