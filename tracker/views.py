from rest_framework import viewsets, filters
from tracker.models import Tracker
from tracker.serializers import TrackerSerializer
from member.models import Elder, CareGiver

# Create your views here.

class trackers(viewsets.ModelViewSet):
	serializer_class = TrackerSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = ('elder',)
	
	def get_queryset(self):
		if CareGiver.objects.filter(user=self.request.user):
			caregiver = CareGiver.objects.get(user=self.request.user)
			return Tracker.objects.filter(elder__in=Elder.get_cared_elder(caregiver))
		elif Elder.objects.filter(user=self.request.user):
			elder = Elder.objects.get(user=self.request.user)
			return Tracker.objects.filter(elder=elder)
		return Tracker.objects.all()
		
