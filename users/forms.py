from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from users.models import Profile


class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control','autocomplete':'off'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control','autocomplete':'off'}))
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

    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
       return self.cleaned_data

    class Meta:
        model = User
        fields = ['first_name', 'last_name','gender','username', 'email', 'password1', 'password2']


class updateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']

    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control','autocomplete':'off'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control','autocomplete':'off'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control','autocomplete':'off'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'E-mail ID', 'class': 'form-control','autocomplete':'off'}))


class updateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img']
    