# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0066_auto_20160421_0630'),
    ]

    operations = [
        migrations.AddField(
            model_name='gcolumn',
            name='format',
            field=models.CharField(choices=[('null', 'Without format'), ('asDays', 'Duraci\xf3n en d\xedas'), ('datetime', 'DD/MM/YYYY, HH:mm'), ('date', 'DD/MM/YYYY')], default='datetime', max_length=30, verbose_name='Format to be used with moment.js'),
        ),
        migrations.AlterField(
            model_name='gcolumn',
            name='content',
            field=models.CharField(choices=[('estimate_time', 'Duration'), ('early_start', 'Early start'), ('last_finish', 'Last Finish')], default='estimate_time', max_length=30, verbose_name='Content of the column'),
        ),
    ]