# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 12:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('neel', '0003_student_roll_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='month',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
