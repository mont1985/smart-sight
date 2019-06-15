from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, HospitalViewSet, PatientViewSet, DoctorsViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'hospitals', HospitalViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]