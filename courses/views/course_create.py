from django.shortcuts import render
from models import Course


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
