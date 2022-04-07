from django import forms
from .models import Laptop
class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'
        labels={
            'brand_name':'Enter Laptop BrandName:',
            'model_name':'Enter Laptop ModelName:',
            'ram':'Enter Laptop RAM(in GB):',
            'rom':'Enter Laptop ROM(in TB):',
            'ssd':'Enter Laptop SSD(in GB):',
            'processor':'Enter Laptop Processor :',
            'os': 'Enter Laptop OS:',
            'price': 'Enter Laptop Price(in INR):'
        }

        widgets = {
            'brand_name': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Dell',
                }
            ),
            'model_name': forms.PasswordInput(),

        }
    def clean_ram(self):
        q = self.cleaned_data['ram']
        if q<=0:
            raise forms.ValidationError('RAM must be at least 1GB!')
        return q

    def clean_price(self):
        p = self.cleaned_data['price']
        if p<=0:
            raise forms.ValidationError('Price can not be less than 1Rs!')
        return p