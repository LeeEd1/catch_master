from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email',
                'phone_number', 'message')

        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'phone_number': 'Your Phone Number (optional)',
            'message': 'Your Message',
        }