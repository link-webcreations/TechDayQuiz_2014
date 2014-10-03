# -*- coding: utf-8 -*-

"""Quiz Restful API views."""

from rest_framework import viewsets
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

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


class QuizResultsView(APIView):
    """View that returns participant results per quizzes."""
    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):
        results = []
        participant_results = {}
        quiz_id = request.GET.get('quiz', None)
        participant_id = request.GET.get('participant', None)

        # Get the quizzes
        if quiz_id:
            quizzes = Quiz.objects.filter(id=quiz_id)
        else:
            quizzes = Quiz.objects.all()

        # Get the participants
        if participant_id:
            participants = Participant.objects.filter(id=participant_id)
        else:
            participants = Participant.objects.all()

        # SHow the results for participants
        for participant in participants:
            participant_results = {
                'participant': participant.fullname,
                'results': [],
            }

            for quiz in quizzes:
                given_anwsers = participant.show_results(quiz.id)
                participant_results['results'].append(given_anwsers)

            results.append(participant_results)

        # Return results JSON serialized
        if results:
            return Response(results)
        else:
            return Response({'error': 'No results found.'},
                            status=status.HTTP_400_BAD_REQUEST)
