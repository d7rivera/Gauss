# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0038_auto_20160401_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gtask_link',
            name='gbaseline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gprojects.Gbaseline'),
        ),
    ]