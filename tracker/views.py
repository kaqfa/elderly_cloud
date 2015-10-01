from rest_framework import viewsets, filters

from tracker.models import Tracker
from tracker.serializers import TrackerSerializer


# Create your views here.

class trackers(viewsets.ModelViewSet):
    serializer_class = TrackerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('elder',)

    def get_queryset(self):
        return Tracker.objects.all()
		
