from rest_framework import viewsets, filters
from notification.models import Notifications
from notification.serializers import NotificationsSerializer
from rest_framework.permissions import AllowAny

# Create your views here.

class notifs(viewsets.ModelViewSet):
	serializer_class = NotificationsSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('elder',)
	
	def get_queryset(self):
		return Notifications.objects.all()
		
