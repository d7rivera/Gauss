# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0055_gtask_lf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gcolumn',
            name='content',
            field=models.CharField(choices=[('estimate_time_days', 'Durationborrar'), ('estimate_time_days', 'Duration'), ('early_start', 'Early startborrar'), ('last_finish', 'Last Finishborrar'), ('es', 'Early start'), ('lf', 'Last Finish')], default='estimate_time_days', max_length=30, verbose_name='Content of the column'),
        ),
    ]
