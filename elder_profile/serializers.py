from rest_framework import serializers
from elder_profile.models import DiseaseHist, MedicalTreatmentHist

class DiseaseHistSerializer(serializers.ModelSerializer):
	class Meta:
		model = DiseaseHist

class MedicalTreatmentHistSerializer(serializers.ModelSerializer):
	class Meta:
		model = MedicalTreatmentHist