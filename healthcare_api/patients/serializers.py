from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'name', 'email', 'phone', 'date_of_birth', 'gender', 'address', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_email(self, value):
        value = value.strip().lower()
        qs = Patient.objects.filter(email__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('A patient with this email already exists.')
        return value

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('Name cannot be empty.')
        return value.strip()
