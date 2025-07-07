from core.views import Api_Crud
from courses.models import CourseEnrollment
from courses.serializers import CourseSerializers



class EnrollmentEdit(Api_Crud):
    queryset = CourseEnrollment.objects.all()
    serializer_class = CourseSerializers