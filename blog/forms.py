from django import forms
from .models import  Profile
from django.contrib.auth.models import User


class UserEditForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly','class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly','class': 'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )

class ProfileEditForm(forms.ModelForm):
    dob = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Profile
        exclude = ('user',)



