from django import forms
from .models import CatchEntry

class CatchEntryForm(forms.ModelForm):
    class Meta:
        model = CatchEntry
        fields = ('name', 'image_url', 
                'image', 'description')