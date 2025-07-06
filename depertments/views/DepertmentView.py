from core.views import Api_Edit, Api_List
from depertments.models import Depertment
from depertments.serializers import DepertmentSerializer

class DepertmentList(Api_Edit, Api_List):
    queryset = Depertment.objects.all()
    serializer_class = DepertmentSerializer