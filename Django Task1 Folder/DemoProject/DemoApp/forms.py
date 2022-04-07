from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels={
            'eno':'Enter Employee No.',
            'ename':'Enter Employee Name:',
            'emob':'Enter Employee Mobile:',
            'edesignation':'Enter Employee Designation:',
            'esal':'Enter Employee Salary:',
            'ecity':'Enter Employee City:',
            'image':'Enter Employee Image:',
}

        widgets = {
            'edesignation': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Engineer',
                }
            ),
            'model_name': forms.PasswordInput(),

        }

    def clean_esal(self):
        s = self.cleaned_data['esal']
        if s<=0:
            raise forms.ValidationError('Salary can not be less than 0Rs or negative!')
        return s

    def clean_eno(self):
        n = self.cleaned_data['eno']
        if n<=0:
            raise forms.ValidationError('Eno can not be less than 1!')
        return n



