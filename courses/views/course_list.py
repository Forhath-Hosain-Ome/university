from rest_framework.response import Response
from rest_framework.decorators import api_view
from courses.serializers import CourseSerializers
from courses.models import Course
from rest_framework import status


@api_view(['GET', 'POST'])
def Course_list(request):
    if request.method == 'POST':
        serializer = CourseSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        courses = Course.objects.all()
        Serializers = CourseSerializers(courses,many=True)
        return Response(Serializers.data, status=status.HTTP_200_OK)
        