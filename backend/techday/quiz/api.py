# -*- coding: utf-8 -*-

"""Quiz Restful API views."""

from rest_framework import viewsets

from .models import Participant, Quiz, Question
from .serializers import (
    ParticipantSerializer,
    QuizSerializer,
    QuestionSerializer,
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
