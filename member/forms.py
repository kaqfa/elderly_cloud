from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from member.models import CareGiver, Elder, CareGiving

class CareGiverForm(forms.ModelForm):
    birthday = forms.DateField(input_formats=['%d/%m/%Y'], required=False)
    class Meta:
        model=CareGiver
        exclude=['user']
        
class UserForm(forms.ModelForm):
    email=forms.EmailField(required=True)
    name=forms.CharField(required=True)
    class Meta:
        model=User
        fields=['username','email','password']
        
    def save(self, commit=True):
        obj = super(UserForm, self).save(commit=False)
        names=self.cleaned_data['name'].split(' ', 1)
        obj.first_name = names[0]
        if len(names)>1:
            obj.last_name = names[1]
        if commit:
            obj.save()
        return obj
        
class CGUserForm(forms.ModelForm):
    name=forms.CharField(required=True)
    class Meta:
        model=User
        fields=['email']
    
    def save(self, commit=True):
        obj = super(CGUserForm, self).save(commit=False)
        names=self.cleaned_data['name'].split(' ', 1)
        obj.first_name = names[0]
        if len(names)>1:
            obj.last_name = names[1]
        else:
            obj.last_name = ''
        if commit:
            obj.save()
        return obj
        
class ElderForm(forms.ModelForm):
    birthday = forms.DateField(input_formats=['%d/%m/%Y'])
    photo = forms.ImageField(required=False)
    class Meta:
        model=Elder
        exclude=['user','code','cared_by']
        
class ElderUserForm(forms.ModelForm):
    name=forms.CharField(required=True)
    class Meta:
        model=User
        fields=[]
        
    def save(self, commit=True):
        obj = super(ElderUserForm, self).save(commit=False)
        names=self.cleaned_data['name'].split(' ', 1)
        obj.first_name = names[0]
        if len(names)>1:
            obj.last_name = names[1]
        else:
            obj.last_name = ''
        if commit:
            obj.save()
        return obj
        
class PartnerForm(forms.ModelForm):
    class Meta:
        model=CareGiver
        fields=['address','phone','photo']
        
class PartnerUserForm(forms.ModelForm):
    email=forms.EmailField(required=True)
    name=forms.CharField(required=True)
    class Meta:
        model=User
        fields=['email']
        
    def save(self, commit=True):
        obj = super(PartnerUserForm, self).save(commit=False)
        names=self.cleaned_data['name'].split(' ', 1)
        obj.first_name = names[0]
        if len(names)>1:
            obj.last_name = names[1]
        else:
            obj.last_name = ''
        if commit:
            obj.save()
        return obj
        
class JoinForm(forms.Form):
    kode = forms.CharField(label='Kode', required=True)
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(JoinForm, self).__init__(*args, **kwargs)
        
    def clean(self):
        cleaned_data = super(JoinForm, self).clean()
        kode = cleaned_data.get('kode')
        if Elder.objects.filter(code=kode):
            elder=Elder.objects.get(code=kode)
            caregiver=CareGiver.objects.get(user=self.request.user)
            if CareGiving.objects.filter(caregiver=caregiver, elder=elder):
                raise forms.ValidationError("Orang tua sudah terdaftar, tidak perlu menambahkan lagi.")
            else:
                return cleaned_data
        else:
            raise forms.ValidationError("Kode tidak terdaftar, silahkan cek kembali.")