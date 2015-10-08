from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='userLogin')
    password = forms.CharField(label='passLogin')