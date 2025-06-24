from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from courses.models import Course
from courses.serializers import CourseSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def course_crud(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_CREATED)
    elif request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_CREATED)
        return Response(serializer.error, status=status.HTTP_200_CREATED)
    elif request.method == 'DELETE':
        course.delete()
        return Response({'message':'Course Deleted'})
    else:
        return Response({'message':'Not Found'})
