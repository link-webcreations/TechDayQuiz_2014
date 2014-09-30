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
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ask', models.CharField(max_length=1024)),
                ('right_answer', models.CharField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(to='quiz.Quiz'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='person',
            field=models.ForeignKey(to='quiz.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='quiz.Question'),
            preserve_default=True,
        ),
    ]
