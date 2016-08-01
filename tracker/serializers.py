from rest_framework import serializers

from tracker.models import Tracker


class TrackerSerializer(serializers.ModelSerializer):
    # elder = serializers.PrimaryKeyRelatedField(required=False,read_only=True)
    photo = serializers.ImageField(use_url=True, required=False)
    modified = serializers.DateField(format='%d/%m/%Y', input_formats=['%d/%m/%Y'], required=False)

    class Meta:
        model = Tracker
