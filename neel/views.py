from django.shortcuts import render
from django.http import HttpResponse
from models import Student, Week, Lecture,  Attendance
from django.template import loader
from forms import AttendanceForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.decorators import csrf
#from django.views.decorators.csrf import csrf_exempt
#from django.core.context_processors import csrf

# Create your views here.

def index(request):
    all_students = Student.objects.all()
    html = ''
    for stu in all_students:
        url = '/neel/' + str(stu.id) + '/'
        html+= '<a href = " ' + url+ ' "> ' + stu.name + ' </a><br>'
    return HttpResponse("<h1> this is timepass...just trying to create a neel</h1><br>" + html)

def index2(request):
    all_students = Student.objects.all()
    template = loader.get_template('neel/index2.html')
    context = {
        'all_students': all_students,
    }
    return HttpResponse(template.render(context, request))

def lecture_template(request , lecture_primary_id , student_roll):
    stu=Student.objects.filter(roll_no = student_roll)[0]
    lec = Lecture.objects.filter (id = lecture_primary_id)[0]
    template = loader.get_template('neel/lecture_template.html')
    context = {
        'stu': stu,
        'lec': lec
    }
    return HttpResponse (template.render(context , request))


def detail (request , student_id):
    return HttpResponse("<h2>hello, student number: "+Student.objects.all()[int(student_id)-1].name+"</h2>")
#we are accessing the name in a roundabout fashion because Student(student_id).name returns a blank unicode string

#@csrf_protect
def attendanceform (request):
    if request.POST:
        form = AttendanceForm (request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/neel/stu1lec1')
    else:
        form = AttendanceForm()

    args = {}
 #   args.update (csrf (request))

    args['form'] = form
    return render_to_response ('neel/create_attendanceform.html' , args)