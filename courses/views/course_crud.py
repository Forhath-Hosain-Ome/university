from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from courses.models import Course
from courses.serializers import CourseSerializers

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def Course_crud(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = CourseSerializers(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CourseSerializers(request.data, instance = course)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = CourseSerializers(request.data, instance = course, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        if course is not None:
            course.delete()
            return Response({'message':'Course Deleted'})
        return Response({'message':'Course Not Found'})
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)