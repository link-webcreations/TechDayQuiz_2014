# -*- coding: utf-8 -*-

"""Quiz REST API module."""

from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
