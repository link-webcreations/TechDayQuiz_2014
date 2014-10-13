# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import quiz.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=1024, null=True, blank=True)),
                ('is_correct', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex=b'^(?u)([^\\W\\d_]|\\s)+$', message=b'Only letters here.', code=b'invalid_lastname')])),
                ('lastname', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex=b'^(?u)([^\\W\\d_]|\\s)+$', message=b'Only letters here.', code=b'invalid_lastname')])),
                ('email', models.EmailField(unique=True, max_length=254, validators=[quiz.validators.validate_email_from_faurecia])),
                ('site', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(regex=b'^(?u)([^\\W\\d_]|\\s)+$', message=b'Only letters here.', code=b'invalid_lastname')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParticipantAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(default=b'', max_length=1024, blank=True)),
                ('answer', models.ForeignKey(blank=True, to='quiz.Answer', null=True)),
                ('participant', models.ForeignKey(related_name=b'given_answers', to='quiz.Participant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=1024)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FreeQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='quiz.Question')),
                ('answer_must_match', models.CharField(help_text=b'The good answer that the participant must provides.', max_length=1024, null=True, blank=True)),
            ],
            options={
            },
            bases=('quiz.question',),
        ),
        migrations.CreateModel(
            name='ChoiceQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='quiz.Question')),
            ],
            options={
            },
            bases=('quiz.question',),
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, editable=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Quizzes',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(related_name=b'questions', to='quiz.Quiz'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participantanswer',
            name='question',
            field=models.ForeignKey(related_name=b'given_answers', to='quiz.Question'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='participantanswer',
            unique_together=set([('participant', 'question')]),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name=b'answers', to='quiz.Question'),
            preserve_default=True,
        ),
    ]
