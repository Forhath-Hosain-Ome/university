from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
    path('admissions/', include('admissons.urls')),
    path('departments/', include('depertments.urls')),
    path('accounts/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('events/', include('events.urls')),
]