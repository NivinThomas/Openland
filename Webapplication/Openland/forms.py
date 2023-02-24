from django import forms
from .models import Registration, Login


class RegisterrForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['owner', 'price', 'address', 'phone_no', 'about', 'zip', 'district']

        widgets = {'district': forms.TextInput(attrs={'class': 'form-control'}),
                   'zip': forms.TextInput(attrs={'class': 'form-control'}),
                   'owner': forms.TextInput(attrs={'class': 'form-control'}),
                   'price': forms.TextInput(attrs={'class': 'form-control'}),
                   'address': forms.TextInput(attrs={'class': 'form-control'}),
                   'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
                   'about': forms.Textarea(attrs={'class': 'form-control'})
                   }


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password']

        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'password': forms.PasswordInput(attrs={'class': 'form-control'}),
                   }


class NewusrForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'

        widgets = {'uname': forms.TextInput(attrs={'class': 'form-control'}),
                   'pass': forms.PasswordInput(attrs={'class': 'form-control'}),
                   'conpass': forms.PasswordInput(attrs={'class': 'form-control'})
                   }
