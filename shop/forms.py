from django import forms
from django.contrib.auth import authenticate,get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

User=get_user_model()

class CreateUserLoginForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']
    
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'input100'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100'}))
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

class CreateUserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'input100'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'input100'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100'}))   
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100'}))   

