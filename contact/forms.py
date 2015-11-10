from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        exclude=['created','modified','status_changed', 'elder', 'added_by']