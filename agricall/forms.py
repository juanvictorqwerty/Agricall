from django import forms
from .models import Products

class ProductForm (forms.ModelForm):

    price = forms.FloatField()
    #image = forms.ImageField
    
    class Meta :

        model = Products

        fields = ['name','description','price','image']

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 0 or price == 0:
            raise forms.ValidationError("Price superior at 0")
        
        return price