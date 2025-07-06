from core.views import Api_Edit, Api_List
from courses.models import Course
from courses.serializers import CourseSerializers

class CourseEdit(Api_Edit, Api_List):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers