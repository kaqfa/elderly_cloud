from rest_framework import viewsets, filters

from elder_profile.models import DiseaseHist, MedicalTreatmentHist
from elder_profile.serializers import DiseaseHistSerializer, MedicalTreatmentHistSerializer
from member.models import Elder, CareGiver


# Create your views here.

class Diseases(viewsets.ModelViewSet):
    serializer_class = DiseaseHistSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('elder',)

    def get_queryset(self):
        if CareGiver.objects.filter(user=self.request.user):
            caregiver = CareGiver.objects.get(user=self.request.user)
            return DiseaseHist.objects.filter(elder__in=Elder.get_cared_elder(caregiver))
        elif Elder.objects.filter(user=self.request.user):
            elder = Elder.objects.get(user=self.request.user)
            return DiseaseHist.objects.filter(elder=elder)
        return DiseaseHist.objects.all()


class MedicalTreatments(viewsets.ModelViewSet):
    serializer_class = MedicalTreatmentHistSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('elder',)

    def get_queryset(self):
        if CareGiver.objects.filter(user=self.request.user):
            caregiver = CareGiver.objects.get(user=self.request.user)
            return MedicalTreatmentHist.objects.filter(elder__in=Elder.get_cared_elder(caregiver))
        elif Elder.objects.filter(user=self.request.user):
            elder = Elder.objects.get(user=self.request.user)
            return MedicalTreatmentHist.objects.filter(elder=elder)
        return MedicalTreatmentHist.objects.all()
