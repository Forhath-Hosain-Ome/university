from django.shortcuts import render
from models import Course


def course_update(id,request):
    if request.method == 'POST':
        form = courseFrom(request.POST, instance = Course.objects.get(pk=id))
        if form.is_valid():
            form.save()
    else:
        form = courseFrom(request.POST, instance=Course.objects.get(pk=id))
    return render(request, 'course/<int:pk>/')
