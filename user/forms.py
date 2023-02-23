from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User

class createUserform(UserCreationForm):
    user_type = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: First Name',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2', 'user_type']