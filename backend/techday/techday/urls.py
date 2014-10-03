from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

from quiz.api import (
    ParticipantAPI,
    ParticipantAnswerAPI,
    QuizAPI,
    QuestionAPI,
    AnswerAPI,
    QuizResultsView,
)

router = routers.DefaultRouter(trailing_slash=False)
router.register('participants', ParticipantAPI)
router.register('quizzes', QuizAPI)
router.register('questions', QuestionAPI)
router.register('answers', AnswerAPI)
router.register('participant_answers', ParticipantAnswerAPI)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/results/$', QuizResultsView.as_view()),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
)
