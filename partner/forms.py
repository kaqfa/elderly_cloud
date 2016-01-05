from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from partner.models import RoomClass, Room, Availability, Agenda

class RoomClassForm(forms.ModelForm):
    class Meta:
        model=RoomClass
        fields=['name','description']

class RoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields=['code','name','roomclass', 'description']
        
class AvailabilityForm(forms.ModelForm):
    class Meta:
        model=Availability
        fields=['num']
        
class AgendaForm(forms.ModelForm):
    duedate = forms.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        model=Agenda
        fields=['duedate','name','description']