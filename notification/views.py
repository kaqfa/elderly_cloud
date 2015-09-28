from rest_framework import viewsets, filters
from notification.models import Notification
from notification.serializers import NotificationSerializer

# Create your views here.

class notifs(viewsets.ModelViewSet):
	serializer_class = NotificationSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('receiver',)
	
	def get_queryset(self):
		return Notification.objects.all()
		
