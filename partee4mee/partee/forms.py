from django.forms import ModelForm
from .models import Party
from django import forms


class PartyForm(forms.ModelForm): 
    class Meta:
        model = Party  
        fields = ["date", "city", "party_type", "free_space",
        "description", "name"]