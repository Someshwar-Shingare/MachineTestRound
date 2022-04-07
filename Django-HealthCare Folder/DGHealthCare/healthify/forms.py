from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Appointment, Ambulance, Doctor, NursingStaff, RoomServiceStaff, Category, Product

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']
        labels = {'email':'Email'}



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

        widgets = {
            'gender': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Male or Female',
                }
            ),
            'previous_visit': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Yes or No',
                }
            ),
            'appointment_date': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. mm/dd/yyyy',
                }
            ),
        }


class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = '__all__'

        widgets = {
            'gender': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Male or Female',
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Aurangabad',
                }
            ),
            'disease': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Jaundice',
                }
            ),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

        widgets = {

            'aadhaar_number': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. 123456789123',
                }
            ),

        }


class NursingStaffForm(forms.ModelForm):
    class Meta:
        model = NursingStaff
        fields = '__all__'

        widgets = {
            'aadhaar_number': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. 123456789123',
                }
            ),

        }

class RoomServiceStaffForm(forms.ModelForm):
    class Meta:
        model = RoomServiceStaff
        fields = '__all__'

        widgets = {
            'address': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Nagpur',
                }
            ),

            'aadhaar_number': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. 123456789123',
                }
            ),

        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Medicine',
                }
            ),

        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }





class FilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all())



