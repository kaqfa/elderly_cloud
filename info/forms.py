from django import forms
from info.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']