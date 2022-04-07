from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=30)
    dob = forms.CharField(max_length=30)
    age = forms.CharField(max_length=30)
    city = forms.CharField(max_length=64)

class ContactForm(forms.Form):
    contactno = forms.IntegerField()
    email = forms.CharField(max_length=30)

