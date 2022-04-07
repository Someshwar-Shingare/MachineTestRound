from django import forms
from django.core import validators

class StudentForm(forms.Form):
    rn = forms.IntegerField(label='Enter Roll No:',validators=[validators.MinValueValidator(1),
                                                               validators.MaxValueValidator(20)])
    name = forms.CharField(max_length=8,label='Enter Full Name:',
                           widget=forms.TextInput(
                               attrs={
                                       'placeholder':'FirstName MiddleNmae LastName'
                                     }
                           )
                           )
    marks = forms.FloatField(label='Enter Marks(out of 100)')
    # password = forms.CharField(max_length=32,
                                 #widget=forms.PasswordInput())
