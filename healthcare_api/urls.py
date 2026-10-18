from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/auth/', include('healthcare_api.auth_api.urls')),
path('api/patients/', include('healthcare_api.patients.urls')),
path('api/doctors/', include('healthcare_api.doctors.urls')),
path('api/mappings/', include('healthcare_api.mappings.urls')),
]
