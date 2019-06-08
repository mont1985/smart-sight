from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, HospitalViewset

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'hospitals', HospitalViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
]