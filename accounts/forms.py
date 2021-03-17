from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Re-password',
        widget=forms.PasswordInput
    )
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control','placeholder': 'Your name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control','placeholder': 'example@gmail.com'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control','placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control','placeholder': 'Re-password'})
    

class UserLoginForm(forms.Form):
    username=forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control','placeholder': 'Your name '})
        self.fields['password'].widget.attrs.update({'class': 'form-control','placeholder': 'Enter Password'})
        
    
