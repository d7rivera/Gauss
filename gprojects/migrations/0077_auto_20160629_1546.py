# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-29 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gprojects', '0076_auto_20160629_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gtask',
            old_name='pessimistic_time',
            new_name='pessimistic_time',
        ),
    ]