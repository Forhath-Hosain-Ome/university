from rest_framework import generics
from courses.models import Course
from courses.serializers import CourseSerializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]



# from rest_framework import generics, mixins


# class CourseMixinView(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializers

#     def get(self, request, pk=None):
#         if pk:
#             return self.retrieve(request, pk=pk)
#         return self.list(request)

#     def post(self, request, *args, **kwargs):
#         return self.create(request)

#     def put(self, request, pk=None):
#         return self.update(request, pk=pk)

#     def patch(self, request, pk=None):
#         return self.partial_update(request, pk=pk)

#     def delete(self, request, pk=None):
#         return self.destroy(request, pk=pk)
