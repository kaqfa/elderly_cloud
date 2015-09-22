from rest_framework import viewsets
from contact.models import Contact
from contact.serializers import ContactSerializer

# Create your views here.

class contacts(viewsets.ModelViewSet):
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer