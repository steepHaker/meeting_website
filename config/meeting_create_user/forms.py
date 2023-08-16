from django import forms
from .models import *




class UserInfoForm(forms.ModelForm):
    class Meta:
       
        model = UserInfo
        fields = '__all__'
        
        widgets = {
            'age': forms.Select(attrs={'class': 'age-spinner'}),
            'myuser': forms.HiddenInput(),
        }
    
   
    age = forms.ChoiceField(label='age',  choices=[(str(age), str(age)) for age in range(18, 101)],
                            widget=forms.Select(attrs={'class': 'age-spinner'}))
    
    height = forms.ChoiceField(label='height', choices=[(str(height),  str(height)) for height in range(100, 300)],
                                        widget=forms.Select(attrs={'class': 'height-spinner'}))
    
    weight = forms.ChoiceField(label='weight',  choices=[(str(weight),  str(weight)) for weight in range(40, 200)],
                                        widget=forms.Select(attrs={'class': 'weight-spinner'}))

    






























class RegistrationForms(forms.ModelForm):
    repeatpassword = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeatpassword']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
            'email': forms.TextInput(attrs={'placeholder': 'email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'password'}),
            'repeatpassword': forms.PasswordInput(attrs={'placeholder': 'repeat password'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


