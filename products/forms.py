from django import forms
from decimal import Decimal
from django.core.exceptions import ValidationError
from .widgets import CustomClearableFileInput
from .models import Product, Category

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'stripe-style-input'

    def clean_price(self):
            price = self.cleaned_data.get('price')

            if price < Decimal('0.01'):
                raise ValidationError("Sorry, the price must be at least 0.01.")

            return price