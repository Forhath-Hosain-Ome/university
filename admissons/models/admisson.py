from core.models import dj_model
from core.models import basemodel, ChoiceConstants
from accounts.models import User
from depertments.models import Depertment
from courses.models import Course



class AdmissonModel(basemodel):
    user = dj_model.ForeignKey(User, on_delete=dj_model.CASCADE, name='user')
    depertment = dj_model.ForeignKey(Depertment, on_delete=dj_model.CASCADE, name='depertment')
    course = dj_model.ForeignKey(Course, on_delete=dj_model.CASCADE, name='course')

    def __str__(self):
        return self.user
    class Meta:
        db_table = 'AdmissonModel'