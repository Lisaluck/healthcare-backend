from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    UserRegistrationView,
    CustomTokenObtainPairView,
    PatientListCreateView,
    PatientRetrieveUpdateDestroyView,
    DoctorListCreateView,
    DoctorRetrieveUpdateDestroyView,
    PatientDoctorMappingListCreateView,
    PatientDoctorMappingRetrieveDestroyView,
    PatientDoctorsListView
)

urlpatterns = [
    # Authentication
    path('auth/register/', UserRegistrationView.as_view(), name='register'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Patient endpoints
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDestroyView.as_view(), name='patient-retrieve-update-destroy'),

    # Doctor endpoints
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view(), name='doctor-retrieve-update-destroy'),

    # Mapping endpoints
    path('mappings/', PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:pk>/', PatientDoctorMappingRetrieveDestroyView.as_view(), name='mapping-retrieve-destroy'),
    path('mappings/<int:patient_id>/', PatientDoctorsListView.as_view(), name='patient-doctors-list'),
]