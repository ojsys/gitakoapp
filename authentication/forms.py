from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class SignUpForm(UserCreationForm):
 
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center', 'placeholder':'password'}),
    )


    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'role')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'last name'}),
            'role': forms.Select(attrs={'class': 'form-control', 'placeholder':'role'}),
        }
        


