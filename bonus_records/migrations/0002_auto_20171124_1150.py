# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 11:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bonus_records', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'ordering': ['-recorded_at']},
        ),
    ]
