from django.conf import settings
from django.db import models
from healthcare_api.patients.models import Patient
from healthcare_api.doctors.models import Doctor

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctor_mappings')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patient_mappings')
    assigned_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='mappings_created')
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['patient', 'doctor'], name='unique_patient_doctor_mapping')
        ]
        ordering = ['-assigned_at']

    def __str__(self):
        return f'{self.patient.name} -> {self.doctor.name}'
