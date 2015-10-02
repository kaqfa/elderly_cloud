from rest_framework import viewsets

from contact.models import Contact
from contact.serializers import ContactSerializer
from member.models import CareGiver, Elder


# Create your views here.

class contacts(viewsets.ModelViewSet):
    serializer_class = ContactSerializer

    def get_queryset(self):
        if CareGiver.objects.filter(user=self.request.user):
            caregiver = CareGiver.objects.get(user=self.request.user)
            return Contact.objects.filter(elder__in=Elder.get_cared_elder(caregiver))
        elif Elder.objects.filter(user=self.request.user):
            elder = Elder.objects.get(user=self.request.user)
            return Contact.objects.filter(elder=elder)
        return Contact.objects.all()
