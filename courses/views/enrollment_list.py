from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from courses.models import CourseEnrollment
from courses.serializers import EnrollmentSerializers

@api_view(['GET', 'POST'])
def enrollment_create(request):
    if request.method == 'GET':
        course = CourseEnrollment.objects.all()
        serializer = EnrollmentSerializers(course, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = EnrollmentSerializers(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)