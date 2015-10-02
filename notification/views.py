from rest_framework import viewsets, filters
from notification.models import Notification, NotificationTemplate
from notification.serializers import NotificationSerializer, NotificationTemplateSerializer
from django.contrib.auth.models import User
from member.models import Elder, CareGiver
from django.db.models import Q

# Create your views here.

class notifs(viewsets.ModelViewSet):
	serializer_class = NotificationSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('receiver',)
	
	def get_queryset(self):
		user = self.request.user
		if CareGiver.objects.filter(user=user):
			caregiver = CareGiver.objects.get(user=user)
			elder = Elder.get_cared_elder(caregiver).values_list('user', flat=True).order_by('id')
			return Notification.objects.filter(Q(sender=user) | Q(receiver=user) | Q(receiver__in=elder))
		elif Elder.objects.filter(user=user):
			elder = Elder.objects.get(user=user)
			caregiver = CareGiver.objects.filter(elder__in=[elder]).values_list('user', flat=True).order_by('id')
			return Notification.objects.filter(Q(sender=user) | Q(receiver=user) | Q(receiver__in=caregiver))
		return Notification.objects.all()
		
class hello(viewsets.ReadOnlyModelViewSet):
	serializer_class = NotificationTemplateSerializer
	
	def get_queryset(self):
		return NotificationTemplate.objects.all()