from rest_framework import serializers

from .models import User, UserProfile, HospitalDoctor, Hospital, PatientDiagnoses, Patient


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('country', 'city', 'address', 'postal_code', 'photo', 'bio')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'title', 'first_name', 'last_name', 'password', 'is_active', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.address = profile_data.get('address', profile.address)
        profile.postal_code = profile_data.get('postal_code', profile.postal_code)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.city = profile_data.get('bio', profile.bio)
        profile.save()
        return instance


class HospitalDoctorSerializer(serializers.PrimaryKeyRelatedField, serializers.ModelSerializer):
    doctor = UserSerializer()

    class Meta:
        model = HospitalDoctor
        fields = ('doctor', 'date_registered')


class HospitalDoctorsSerializer(serializers.ModelSerializer):
    doctor = UserSerializer()

    class Meta:
        model = HospitalDoctor
        fields = ('doctor',)


class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    doctors = HospitalDoctorSerializer(many=True, queryset=User.objects.filter(title='DOCTOR'))
    administrator = UserSerializer(read_only=True)
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Hospital
        fields = ('url', 'name', 'country', 'address', 'postal_code', 'level', 'administrator', 'doctors', 'owner')

    def create(self, validated_data):
        doctors_data = validated_data.pop('doctors')
        admin = validated_data.pop('owner')  # get admin from logged in user
        hospital = Hospital(administrator=admin, **validated_data)
        hospital.save()  # create hospital

        for doctor in doctors_data:
            HospitalDoctor.objects.create(hospital=hospital, doctor=doctor)
        return hospital

    def update(self, instance, validated_data):
        stored_doctors = list(instance.doctors.all())
        update_doctors = validated_data.pop('doctors')
        # update hospital
        import pdb; pdb.set_trace()
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.address = validated_data.get('address', instance.address)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.level = validated_data.get('level', instance.level)
        instance.save()

        # prepare id for doctors
        stored_doctors_ids = [x.doctor.id for x in stored_doctors]
        update_doctors_ids = [x.id for x in update_doctors]

        # if doctor exists keep else delete
        for doctor in stored_doctors:
            if doctor.doctor.id not in update_doctors_ids:
                doctor.delete()
        # if new doctor create and add doctor.
        for doctor in update_doctors:
            if doctor.id not in stored_doctors_ids:
                HospitalDoctor.objects.create(hospital=instance, doctor=doctor)

        return instance


class DiagnosisSerializer(serializers.ModelSerializer):
    hospital_visited = HospitalSerializer()
    doctor = UserSerializer()

    class Meta:
        model = PatientDiagnoses
        fields = ('image', 'model_diagnosis', 'is_true', 'doctors_comment', 'doctor', 'hospital_visited')


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    diagnosis = DiagnosisSerializer(many=True)

    class Meta:
        model = Patient
        fields = (
            'name', 'age', 'gender', 'identification', 'email', 'contact',
            'marital_status', 'county', 'address', 'postal_code', 'diagnosis')
# overide create and update methods for all serializers
