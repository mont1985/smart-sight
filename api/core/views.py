from rest_framework import viewsets

from .models import User, Hospital
from .serializers import UserSerializer, HospitalSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HospitalViewset(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
