from django import forms
from .models import Student

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        #fields = ['company','model_name']
        #exclude = ['price']