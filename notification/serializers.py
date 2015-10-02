from rest_framework import serializers

from notification.models import NotificationTemplate
from notification.models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification


class NotificationTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationTemplate
