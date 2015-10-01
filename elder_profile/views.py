from rest_framework import viewsets, filters

from elder_profile.models import DiseaseHist, MedicalTreatmentHist
from elder_profile.serializers import DiseaseHistSerializer, MedicalTreatmentHistSerializer


# Create your views here.

class diseases(viewsets.ModelViewSet):
    serializer_class = DiseaseHistSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('elder',)

    def get_queryset(self):
        return DiseaseHist.objects.all()


class medicalTreatments(viewsets.ModelViewSet):
    serializer_class = MedicalTreatmentHistSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('elder',)

    def get_queryset(self):
        return MedicalTreatmentHist.objects.all()
		