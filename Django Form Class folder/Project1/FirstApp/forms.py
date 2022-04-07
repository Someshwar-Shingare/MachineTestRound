from django import forms

class StudentForm(forms.Form):
    rn = forms.IntegerField()
    name = forms.CharField(max_length=3)
    marks = forms.FloatField()
    city = forms.CharField(max_length=64)