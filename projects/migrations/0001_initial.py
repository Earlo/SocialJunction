# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('data_date', models.DateTimeField(verbose_name=b'When?')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event',
            field=models.ForeignKey(to='projects.Project'),
        ),
        migrations.AddField(
            model_name='date',
            name='Project',
            field=models.ForeignKey(to='projects.Project'),
        ),
        migrations.AddField(
            model_name='date',
            name='event',
            field=models.ForeignKey(to='projects.Event'),
        ),
    ]
