from django import forms
from user.models import Kaam


class KaamForm(forms.ModelForm):
    class Meta:
     model = Kaam
     fields = ['title', 'description', 'completed']