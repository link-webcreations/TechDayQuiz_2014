# -*- coding: utf-8 -*-

from django.contrib import admin

import models
from .forms import AnswerInlineFormset


class TechdayAdminSite(admin.sites.AdminSite):
    site_header = "TechDay Administration"
    site_title = "TechDay Admin Site"


class QuestionAnswerInline(admin.StackedInline):
    model = models.Answer
    extra = 1
    formset = AnswerInlineFormset


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created')
    list_filter = ('created',)

    def save_model(self, request, obj, *args, **kwargs):
        obj.author = request.user
        obj.save()


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'quiz')
    list_filter = ('quiz__name',)
    inlines = (QuestionAnswerInline, )

admin_site = TechdayAdminSite()
admin_site.register(models.Quiz, QuizAdmin)
admin_site.register(models.Question, QuestionAdmin)
