from django import forms
from user.models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
     model =Register
     fields = ['name', 'email', 'password1', 'password2']