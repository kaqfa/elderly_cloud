from django import forms
from feedback.models import Feedback, Response

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        exclude=['status', 'status_changed', 'owner']
        
class ResponseForm(forms.ModelForm):
    class Meta:
        model=Response
        exclude=['feedback', 'owner']