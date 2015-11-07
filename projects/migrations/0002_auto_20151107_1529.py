# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='date',
            name='Project',
        ),
        migrations.RemoveField(
            model_name='date',
            name='event',
        ),
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'Date of happening'),
        ),
        migrations.DeleteModel(
            name='Date',
        ),
    ]
