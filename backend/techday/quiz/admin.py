# -*- coding: utf-8 -*-

from django.contrib import admin

import models


class TechdayAdminSite(admin.sites.AdminSite):
    site_header = "TechDay Administration"
    site_title = "TechDay Admin Site"


class QuestionAnswerInline(admin.StackedInline):
    model = models.Answer
    extra = 1


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'created')
    list_filter = ('created',)

    def save_model(self, request, obj, *args, **kwargs):
        obj.author = request.user
        obj.save()


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'quiz')
    list_filter = ('quiz__name',)


class ChoiceQuestionAdmin(QuestionAdmin):
    inlines = (QuestionAnswerInline, )

admin_site = TechdayAdminSite()
admin_site.register(models.Quiz, QuizAdmin)
admin_site.register(models.ChoiceQuestion, ChoiceQuestionAdmin)
admin_site.register(models.FreeQuestion, QuestionAdmin)
