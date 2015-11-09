from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from notification.models import Notification

class NotificationForm(forms.ModelForm):
    invoked_on = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    class Meta:
        model=Notification
        exclude=['responded', 'sender', 'receiver', 'status', 'status_changed']