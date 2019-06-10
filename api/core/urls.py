from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, HospitalViewSet, DoctorsViewSet, PatientViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'hospitals', HospitalViewSet)
router.register(r'doctors', DoctorsViewSet)
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]