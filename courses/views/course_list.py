from rest_framework.response import Response
from rest_framework.decorators import api_view
from courses.serializers import CourseSerializer
from courses.models import Course
from rest_framework import status


@api_view(['GET', 'POST'])
def course_list(request):
    if request.method == 'POST':
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_CREATED)
        return Response(serializer.error, status=status.HTTP_200_CREATED)
    elif request.method == "GET":
        Courses = Course.objects.all()
        Serializers = CourseSerializer(Courses,many=True)
        return Response(Serializers.data, status=status.HTTP_200_CREATED)
        


# def course_create(request):
#     if request.method == 'POST':
#         form = courseFrom(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(request, 'courses/course_list.html',)
#             #return redirect('courses:course_detail', pk=form.instance.pk)
#     else:
#         form = courseFrom()
#     return render(request, 'courses/course_form.html', {'form': form})
