from rest_framework import viewsets
from .models import User, Hospital, Patient, HospitalDoctor
from .serializers import UserSerializer, HospitalSerializer, PatientSerializer, HospitalDoctorsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class DoctorsViewSet(viewsets.ModelViewSet):
    queryset = HospitalDoctor.objects.all()
    serializer_class = HospitalDoctorsSerializer

