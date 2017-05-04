from __future__ import unicode_literals
from django.db import models
import ast
import simplejson as json

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 200)
    age = models.IntegerField()
    gender = models.CharField(max_length = 1)
    native_place = models.CharField(max_length = 200)
    designation = models.CharField(max_length = 30)
    posting_place = models.CharField(max_length = 30)
    MDFF = models.CharField(max_length = 30)
    ST = models.CharField(max_length = 30)
    OJT = models.CharField(max_length = 30)
    roll_no = models.IntegerField()
    password = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.roll_no)

class Week (models.Model):
    starting = models.DateField()
    ending = models.DateField()
    week_number = models.IntegerField()

    def __str__(self):
        return "Week " + str(self.week_number)

class Lecture (models.Model):
    week = models.ForeignKey(Week )
    #we do not add on_delete = models.CASCADE because deleting a week does not imply lectures should be deleted
    name_of_lecturer = models.CharField(max_length = 200)
    topic = models.CharField(max_length = 100)
    #day = models.IntegerField()
    date = models.DateField()
    time = models.IntegerField()

    def __str__(self):
        return self.topic