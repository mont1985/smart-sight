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
        extra_kwargs = {'password': {'write_only': True}}

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


class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    doctors = HospitalDoctorSerializer(many=True, queryset=User.objects.filter(title='DOCTOR'))
    administrator = UserSerializer(read_only=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

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


class HospitalDoctorsSerializer(serializers.ModelSerializer):
    doctor = UserSerializer()
    hospital = HospitalSerializer()

    class Meta:
        model = HospitalDoctor
        fields = ('hospital', 'doctor')


class DiagnosisSerializer(serializers.ModelSerializer):
    hospital_visited = HospitalSerializer()
    doctor = UserSerializer()

    class Meta:
        model = PatientDiagnoses
        fields = ('image', 'model_diagnosis', 'is_true', 'doctors_comment', 'doctor', 'hospital_visited')


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    diagnosis = DiagnosisSerializer(many=True, read_only=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    hospital = serializers.IntegerField(write_only=True, required=False)
    image = serializers.ImageField(write_only=True, required=False)
    is_true = serializers.BooleanField(default=False, write_only=True)
    comment = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Patient
        fields = ('url', 'name', 'age', 'gender', 'identification', 'email', 'contact',
                  'marital_status', 'county', 'address', 'postal_code', 'diagnosis',
                  'owner', 'hospital', 'image', 'is_true', 'comment')

    def create(self, validated_data):
        comment = validated_data.get('comment', None)
        is_true = validated_data.get('is_true', None)
        image = validated_data.pop('image')
        hospital = validated_data.pop('hospital')
        doctor = validated_data.pop('owner')
        validated_data.pop('is_true')
        if comment:
            validated_data.pop('comment')

        patient = Patient(**validated_data)
        patient.save()

        diagnosis_data = {
            'patient': patient,
            'image': image,
            'is_true': is_true,
            'doctors_comment': comment,
            'hospital_visited': Hospital.objects.get(id=hospital),
            'doctor': doctor
        }
        diagnosis = PatientDiagnoses(**diagnosis_data)
        diagnosis.save()

        return patient

    def update(self, instance, validated_data):
        diagnosis = list(instance.diagnosis.all())[0]

        # update user
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.identification = validated_data.get('identification', instance.identification)
        instance.email = validated_data.get('email', instance.email)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.marital_status = validated_data.get('marital_status', instance.marital_status)
        instance.county = validated_data.get('county', instance.county)
        instance.address = validated_data.get('address', instance.address)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.save()

        # update diagnosis
        diagnosis.is_true = validated_data.get('is_true', diagnosis.is_true)
        diagnosis.doctors_comment = validated_data.get('comment', diagnosis.doctors_comment)
        diagnosis.save()

        return instance
