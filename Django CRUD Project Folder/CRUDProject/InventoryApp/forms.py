from django import forms
from .models import Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels={
            'category':'Enter Product Category',
            'company':'Enter Product Company:',
            'name':'Enter Product Name:',
            'qty':'Enter Product Quantity:',
            'price':'Enter Product Price:'
        }
    def clean_qty(self):
        q = self.cleaned_data['qty']
        if q<=0:
            raise forms.ValidationError('Quantity must be at least 1!')
        return q

    def clean_price(self):
        p = self.cleaned_data['price']
        if p<=0:
            raise forms.ValidationError('Price can not be less than 1Rs!')
        return p