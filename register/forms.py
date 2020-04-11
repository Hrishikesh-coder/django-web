from django import forms
from django.core import validators

class SignUp(forms.Form):
    first_name = forms.CharField(initial='First Name',)
    last_name = forms.CharField()
    email = forms.EmailField(help_text = 'Write your email',)
    
    Address = forms.CharField(required = False, )
    Technology = forms.CharField(initial = 'Django', disabled = True, )

    age = forms.IntegerField()
    password = forms.CharField(widget = forms.PasswordInput, validators = [validators.MinLengthValidator(6)])    
    re_password = forms.CharField(help_text='reenter your password',
    widget=forms.PasswordInput)
