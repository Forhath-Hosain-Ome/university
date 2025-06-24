from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from courses.models import CourseEnrollment
from courses.serializers import CourseSerializers

@api_view(['GET', 'PUT', 'DELETE'])
def enrollment_edit(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        pass