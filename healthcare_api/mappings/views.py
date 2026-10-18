from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from healthcare_api.patients.models import Patient
from .models import PatientDoctorMapping
from .serializers import MappingCreateSerializer, MappingSerializer

class MappingListCreateView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.select_related('patient', 'doctor').all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return MappingCreateSerializer if self.request.method == 'POST' else MappingSerializer

    def perform_create(self, serializer):
        serializer.save(assigned_by=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mapping = serializer.save(assigned_by=request.user)
        return Response(MappingSerializer(mapping).data, status=status.HTTP_201_CREATED)

class PatientMappingsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        patient = get_object_or_404(Patient, pk=patient_id)
        mappings = PatientDoctorMapping.objects.select_related('doctor').filter(patient=patient)
        return Response({
            'patient': {'id': patient.id, 'name': patient.name},
            'doctors': [
                {
                    'mapping_id': m.id,
                    'id': m.doctor.id,
                    'name': m.doctor.name,
                    'specialization': m.doctor.specialization,
                    'email': m.doctor.email,
                }
                for m in mappings
            ]
        })

    def delete(self, request, patient_id):
        # The assignment defines DELETE /api/mappings/<id>/ where <id> is the mapping id.
        mapping = get_object_or_404(PatientDoctorMapping, pk=patient_id)
        mapping.delete()
        return Response({'message': 'Doctor removed from patient successfully.'}, status=status.HTTP_204_NO_CONTENT)
