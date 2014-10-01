# -*- coding: utf-8 -*-

"""Quiz app forms."""

from django import forms


class AnswerInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            try:
                if form.cleaned_data:
                    count += 1
            except AttributeError:
                pass
        if count < 1:
            raise forms.ValidationError('You must have at least one answer !')
