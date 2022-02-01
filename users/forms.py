from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import request

from users.models import Profile


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control','autocomplete':'off'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control','autocomplete':'off'}))
    # enrollment = forms.CharField(max_length=10, un)
    # DOB = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Date of Birth', 'class': 'form-control'}))
    GENDER_CHOICES = (
        ('NA', 'Not defined'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control','autocomplete':'off'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-select', 'autocomplete': 'off'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail ID', 'class': 'form-control','autocomplete':'off'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-control' ,'autocomplete':'off'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-control','autocomplete':'off'}))



    class Meta:
        model = User
        fields = ['first_name', 'last_name','gender','username', 'email', 'password1', 'password2']


class updateUserForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email','username']

class updateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img']