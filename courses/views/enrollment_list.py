from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from courses.models import CourseEnrollment
from courses.serializers import CourseSerializers

@api_view(['GET', 'POST'])
def enrollment_list(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    else:
        pass