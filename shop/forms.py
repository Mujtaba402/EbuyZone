from django import forms
from django.contrib.auth.models import User

from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Text goes here!!!', 'rows': '2', 'cols': '150'}))

    class Meta:
        model = Comment
        fields = {
            'content',
        }
