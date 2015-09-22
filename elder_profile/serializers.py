from rest_framework import serializers
from elder_profile.models import DiseaseHist, MedicalTreatmentHist

class DiseaseHistSerializer(serializers.ModelSerializer):
	class Meta:
		model = DiseaseHist
		fields = ('id', 'elder', 'name')

class MedicalTreatmentHistSerializer(serializers.ModelSerializer):
	class Meta:
		model = MedicalTreatmentHist
		fields = ('id', 'elder', 'treatment')