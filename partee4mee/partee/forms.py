from django.forms import ModelForm
from .models import Party

class PartyForm(ModelForm):
    
    class Meta:
        model = Party  
        fields = ["date", "city", "party_type", "free_space",
        "description", "name"]