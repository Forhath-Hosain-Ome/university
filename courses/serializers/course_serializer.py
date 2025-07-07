from core.serializers import rf_ModelSerializer
from courses.models import Course

class CourseSerializers(rf_ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'