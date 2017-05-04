from django.shortcuts import render
from django.http import HttpResponse
from models import Student, Week, Lecture
from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


def index2(request):
    all_students = Student.objects.all()
    template = loader.get_template('ONGC_A/index2.html')
    context = {
        'all_students': all_students,
    }
    return HttpResponse(template.render(context, request))


def lecture_template(request, lecture_primary_id, student_roll):
    stu=Student.objects.filter(roll_no=student_roll)[0]
    lec = Lecture.objects.filter(id=lecture_primary_id)[0]
    template = loader.get_template('ONGC_A/lecture_template.html')
    context = {
        'stu': stu,
        'lec': lec
    }
    return HttpResponse (template.render(context , request))


def detail(request, student_id):
    return HttpResponse("<h2>hello, student number: "+Student.objects.all()[int(student_id)-1].name+"</h2>")
