from rest_framework import serializers
from .models import PatientDoctorMapping

class MappingSerializer(serializers.ModelSerializer):
    patient_id = serializers.IntegerField(source='patient.id', read_only=True)
    doctor_id = serializers.IntegerField(source='doctor.id', read_only=True)
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ('id', 'patient_id', 'doctor_id', 'patient_name', 'doctor_name', 'assigned_at')
        read_only_fields = fields

class MappingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = ('patient', 'doctor')

    def validate(self, attrs):
        if PatientDoctorMapping.objects.filter(patient=attrs['patient'], doctor=attrs['doctor']).exists():
            raise serializers.ValidationError('This doctor is already assigned to this patient.')
        return attrs
