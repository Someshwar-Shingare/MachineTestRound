from django import forms

class StudentForm(forms.Form):
    rn = forms.IntegerField()
    name = forms.CharField(max_length=30)
    marks = forms.FloatField()
