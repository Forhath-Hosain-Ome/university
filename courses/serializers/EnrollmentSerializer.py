from courses.models import CourseEnrollment
from core.serializers import rf_ModelSerializer

class EnrollmentSerializers(rf_ModelSerializer):
    class Meta:
        model = CourseEnrollment
        fields = '__all__'