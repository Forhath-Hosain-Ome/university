from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('admissions/', include('admissons.urls')),
    path('departments/', include('depertments.urls')),
    path('accounts/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('events/', include('events.urls')),
]

# urlpatterns += [
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]