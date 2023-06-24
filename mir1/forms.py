from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
from .models import users

class SignUP(UserCreationForm):
    user_id = forms.CharField(max_length=100)           
    user_name= forms.CharField(max_length=100)
    email = forms.EmailField(max_length=50)
    user_state = forms.EmailField(max_length=100)
    phone_number = forms.IntegerField()
    class Meta():
        model = User
        fields = ('user_id','user_name', 'email', 'password1','password2','user_state','phone_number','email') 