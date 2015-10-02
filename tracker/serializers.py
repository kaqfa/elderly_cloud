from rest_framework import serializers

from tracker.models import Tracker


class TrackerSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(use_url=True)

    class Meta:
        model = Tracker