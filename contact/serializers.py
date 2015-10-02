from rest_framework import serializers

from contact.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'elder', 'added_by', 'name', 'address', 'phone', 'email', 'status')