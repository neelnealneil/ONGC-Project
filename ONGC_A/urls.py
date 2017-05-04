from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$' , views.index2, name = 'index2'),
    url(r'^(?P<student_id>[0-9]+)/$' , views.detail , name='detail'),
    url(r'^lec(?P<lecture_primary_id>[0-9]+)stu(?P<student_roll>[0-9]+)/$' , views.lecture_template , name = 'lecture_template'),

]