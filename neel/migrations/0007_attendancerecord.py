# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 05:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('neel', '0006_week_week_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('L', 'Leave')], max_length=1)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neel.Lecture')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neel.Student')),
            ],
        ),
    ]
