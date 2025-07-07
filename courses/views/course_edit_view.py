from core.views import Api_Crud
from courses.models import Course
from courses.serializers import CourseSerializers

class CourseEdit(Api_Crud):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers