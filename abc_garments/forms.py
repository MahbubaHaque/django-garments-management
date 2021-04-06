from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Employee,Notification

class EmployeeForm(forms.ModelForm):

    class Meta:
        model=Employee
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supervisor'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control','placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control','placeholder': 'Last Name'})
        self.fields['salary'].widget.attrs.update({'class': 'form-control','placeholder': 'salary'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control','placeholder': 'phone number'})


class NotificationForm(forms.ModelForm):

    class Meta:
        model=Notification
        fields='__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'class': 'form-control','placeholder': 'write message'})