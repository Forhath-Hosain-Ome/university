from django import forms
from .models import *

class registerForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password','class' : 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Account.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Account.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username
    
class login_Auth(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'password']