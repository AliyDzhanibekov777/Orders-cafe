from django import forms
from .models import Dishes


class MenuForm(forms.ModelForm):
    class Meta:
        model = Dishes
        fields = ('name', 'price')