# -*- coding: utf-8 -*-

"""Quiz Restful API views."""

from rest_framework import viewsets

from .models import (
    Participant,
    ParticipantAnswer,
    Quiz,
    Question,
    Answer,
)
from .serializers import (
    ParticipantSerializer,
    ParticipantAnswerSerializer,
    QuizSerializer,
    QuestionSerializer,
    AnswerSerializer,
)


class ParticipantAPI(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class QuizAPI(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionAPI(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_fields = ('quiz',)


class AnswerAPI(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class ParticipantAnswerAPI(viewsets.ModelViewSet):
    queryset = ParticipantAnswer.objects.all()
    serializer_class = ParticipantAnswerSerializer
