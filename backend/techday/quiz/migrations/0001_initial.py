# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import quiz.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex=b'^(?u)([^\\W\\d_]|\\s)+$', message=b'Only letters here.', code=b'invalid_lastname')])),
                ('lastname', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex=b'^(?u)([^\\W\\d_]|\\s)+$', message=b'Only letters here.', code=b'invalid_lastname')])),
                ('email', models.EmailField(unique=True, max_length=254, validators=[quiz.validators.validate_email_from_faurecia])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
