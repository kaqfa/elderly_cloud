from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from elder_profile.models import MedicalTreatmentHist, DiseaseHist

class MedicalTreatmentForm(forms.ModelForm):
    class Meta:
        model=MedicalTreatmentHist
        exclude=['created','modified','status_changed', 'elder']

class DiseaseHistForm(forms.ModelForm):
    class Meta:
        model=DiseaseHist
        exclude=['created','modified','status_changed', 'elder']