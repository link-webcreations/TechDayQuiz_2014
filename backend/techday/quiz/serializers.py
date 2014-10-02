# -*- coding: utf-8 -*-

"""Quiz REST API module."""

from rest_framework import serializers

from .models import Participant, Quiz, Answer, Question


class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participant


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('content',)


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('content', 'answers')


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'name', 'created')
