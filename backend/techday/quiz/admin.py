# -*- coding: utf-8 -*-

from django.contrib import admin

import models
from .forms import AnswerInlineFormset


class QuestionAnswerInline(admin.StackedInline):
    model = models.Answer
    extra = 1
    formset = AnswerInlineFormset


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created')
    list_filter = ('created',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'quiz')
    list_filter = ('quiz__name',)
    inlines = (QuestionAnswerInline, )


admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.Question, QuestionAdmin)
