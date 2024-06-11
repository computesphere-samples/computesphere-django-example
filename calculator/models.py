from django.db import models
from django import forms

class DateForm(forms.Form):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
