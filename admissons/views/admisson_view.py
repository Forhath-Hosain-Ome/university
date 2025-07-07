from core.views import Api_Crud
from admissons.models import AdmissonModel
from admissons.serializers import AdmissonSerializer

class AdmissonList(Api_Crud):
    queryset = AdmissonModel.objects.all()
    serializer_class = AdmissonSerializer