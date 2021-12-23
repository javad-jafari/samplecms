from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
User = get_user_model()

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='pass', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confim pass', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

