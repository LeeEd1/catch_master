from django import forms
from .models import CatchEntry

class CatchEntryForm(forms.ModelForm):
    class Meta:
        model = CatchEntry
        fields = ('image', 'description')