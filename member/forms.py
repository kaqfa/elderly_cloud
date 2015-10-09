from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from member.models import CareGiver, Elder

class CareGiverForm(forms.ModelForm):
    birthday = forms.DateField(input_formats=['%m/%d/%Y'])
    class Meta:
        model=CareGiver
        exclude=['user']
        
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']