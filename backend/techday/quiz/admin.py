# -*- coding: utf-8 -*-

from django.contrib import admin

import models


class PersonAdmin(admin.ModelAdmin):
    """Customize the layout of Person model."""
    list_display = ('firstname', 'lastname', 'email')
    list_display_links = ('firstname', 'email')
    fieldsets = (
        ('Identity', {'fields': ('firstname', 'lastname')}),
        (None, {'fields': ('email',)})
    )

admin.site.register(models.Person, PersonAdmin)
