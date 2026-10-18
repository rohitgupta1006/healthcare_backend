from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('id', 'name', 'email', 'phone', 'specialization', 'license_number', 'experience_years', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_email(self, value):
        value = value.strip().lower()
        qs = Doctor.objects.filter(email__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('A doctor with this email already exists.')
        return value

    def validate_experience_years(self, value):
        if value > 70:
            raise serializers.ValidationError('Experience years must be 70 or less.')
        return value

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('Name cannot be empty.')
        return value.strip()
