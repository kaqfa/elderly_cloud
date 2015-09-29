from rest_framework import serializers
from notification.models import Notification, NotificationTemplate

class NotificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notification
		
class NotificationTemplateSerializer(serializers.ModelSerializer):
	class Meta:
		model = NotificationTemplate