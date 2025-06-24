from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from courses.models import CourseEnrollment
from courses.serializers import CourseSerializers


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def enrollment_crud(request,pk):
    course = CourseEnrollment.objects.get(pk=pk)
    serializer = CourseSerializers(course)
    if request.method == 'GET':
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = CourseSerializers(course, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PATCH':
        serializer = CourseSerializers(course, request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)