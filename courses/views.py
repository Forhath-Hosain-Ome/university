from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def course(request):
    course = Course.objects.all()
    return render(request, 'courses/course_list.html', {'course' : course} )

def course_detail(request, pk):
    details = Course.objects.get(pk=pk)
    return render(request, 'courses/course_detail.html', {'details': details})

def course_create(request):
    if request.method == 'POST':
        form = courseFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'courses/course_list.html',)
            #return redirect('courses:course_detail', pk=form.instance.pk)
    else:
        form = courseFrom()
    return render(request, 'courses/course_form.html', {'form': form})

def course_update(id,request):
    if request.method == 'POST':
        form = courseFrom(request.POST, instance = Course.objects.get(pk=id))
        if form.is_valid():
            form.save()
    else:
        form = courseFrom(request.POST, instance=Course.objects.get(pk=id))
    return render(request, 'course/<int:pk>/')

def course_delete(id,request):
    pass