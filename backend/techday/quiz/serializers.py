# -*- coding: utf-8 -*-

"""Quiz Restful API model serialization."""

from django.conf import settings
from rest_framework import serializers

from .models import (
    Participant,
    ParticipantAnswer,
    Quiz,
    Answer,
    Question,
)


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participant
        fields = ('url', 'id', 'firstname', 'lastname', 'email', 'site',)


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'question', 'content', 'match_given')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'content', 'answers',)


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'name', 'created',)


class ParticipantAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantAnswer
        fields = ('id', 'participant', 'answer', 'content')
        if not settings.DEBUG:
            write_only_fields = ('answer', 'content',)
