from django import forms
from .models import Laptop

class LaptopModelForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = '__all__'
        #fields = ['company','model_name']
        #exclude = ['price']
        labels = {
                   'ram':'Enter RAM(in GB):',
                   'price':'Enter Price in INR:'
        }
        widgets = {
            'company':forms.TextInput(
                attrs={
                    'placeholder':'e.g. Dell',
                }
            ),
            'model_name':forms.PasswordInput(),

        }
    def clean_ram(self):
        user_entered_ram = self.cleaned_data['ram']
        if user_entered_ram<1:
            raise forms.ValidationError('RAM can not be less than 1GB')
        return user_entered_ram

    def clean(self):
        all_data = super().clean()
        user_entered_rom = all_data['rom']
        if user_entered_rom<1:
            raise forms.ValidationError('ROM can not be less than 1GB')
        # return user_entered_rom
        user_entered_price = all_data['price']
        if user_entered_price<0:
            raise forms.ValidationError('Price can not be less than 0Rs')
        # return user_entered_price

