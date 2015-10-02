from rest_framework import serializers

from info.models import Posting


class PostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posting