from django import forms
from django.core import validators

class StudentForm(forms.Form):
    rn = forms.IntegerField(validators=[validators.MinValueValidator(1),
                                        validators.MaxValueValidator(20)])
    name = forms.CharField(max_length=8)
    marks = forms.FloatField()