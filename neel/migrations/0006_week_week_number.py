# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neel', '0005_auto_20170228_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='week_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]