from django import forms
from django.contrib.auth import authenticate
from member.models import CareGiver, Elder, Partner

class LoginForm(forms.Form):
    username = forms.CharField(label='userLogin', required=True)
    password = forms.CharField(label='passLogin', required=True)
    
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)        
        if ( not user or 
             not user.is_active or                
             not (CareGiver.objects.filter(user=user) or  
                  Partner.objects.filter(user=user) or user.is_staff )):                        
            raise forms.ValidationError("Username/password salah, silahkan coba lagi.")        

        return cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
