# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neel', '0004_lecture_month'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='month',
            new_name='date',
        ),
        migrations.AddField(
            model_name='lecture',
            name='time',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='adsf', max_length=20),
            preserve_default=False,
        ),
    ]