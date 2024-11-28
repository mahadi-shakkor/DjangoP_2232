

from django import forms
from .models import User, Location
class SignupForm(forms.Form):
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(max_length=255, required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    password = forms.CharField(max_length=255, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    usercontactnumber = forms.CharField(max_length=15, required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter contact number'}))
    
    USER_TYPE_CHOICES = [
        ('a', 'Aggri Officer'),
        ('n', 'Neutroshonist'),
        ('r', 'Retailer'),
        ('w', 'Wirehouse manager'),
        ('s', 'Supplier'),
        ('d', 'Distributor Company'),
        ('c', 'Customer'),
        ('f', 'Farmer'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True, widget=forms.Select)
