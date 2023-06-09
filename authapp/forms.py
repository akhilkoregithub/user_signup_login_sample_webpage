from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegistration(forms.ModelForm):
    password=forms.CharField(label="password", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repeat Password", widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=('username','first_name','last_name','email')
        
        def clean_password2(self):
            cd==self.cleaned_data
            if cd['password']!=cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
        
    