from rest_framework import viewsets, filters
from notification.models import Notification, NotificationTemplate
from notification.serializers import NotificationSerializer, NotificationTemplateSerializer

# Create your views here.

class notifs(viewsets.ModelViewSet):
	serializer_class = NotificationSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('receiver',)
	
	def get_queryset(self):
		return Notification.objects.all()
		
class hello(viewsets.ReadOnlyModelViewSet):
	serializer_class = NotificationTemplateSerializer
	
	def get_queryset(self):
		return NotificationTemplate.objects.all()