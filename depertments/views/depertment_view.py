from core.views import Api_Crud
from depertments.models import Depertment
from depertments.serializers import DepertmentSerializer

class DepertmentList(Api_Crud):
    queryset = Depertment.objects.all()
    serializer_class = DepertmentSerializer