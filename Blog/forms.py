from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control','autocomplete':'off'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control','autocomplete':'off'}))
    # enrollment = forms.CharField(max_length=10, un)
    # DOB = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Date of Birth', 'class': 'form-control'}))
    GENDER_CHOICES = (
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
        exclude = ('password2.help_text',)
