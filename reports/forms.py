from django.forms import ModelForm
from django import forms
from .models import benefits

class addbenefit():
    stateid = forms.CharField(max_length=2)
    statename = forms.CharField(max_length= 20)
    Target = forms.CharField(max_length=10)
    profit_amount = forms.CharField(max_length=10)


