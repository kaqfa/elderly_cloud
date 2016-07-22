from rest_framework import serializers

from hospital.models import Hospital

class HospitalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hospital