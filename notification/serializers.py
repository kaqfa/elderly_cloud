from rest_framework import serializers
from notification.models import Notifications

class NotificationsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Notifications
		fields = ('id', 'elder', 'title', 'content')