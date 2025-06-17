from django.shortcuts import render
from models import Course


def course(request):
    course = Course.objects.all()
    return render(request, 'courses/course_list.html', {'course' : course} )