from django.shortcuts import render
from models import Course

def course_detail(request, pk):
    details = Course.objects.get(pk=pk)
    return render(request, 'courses/course_detail.html', {'details': details})