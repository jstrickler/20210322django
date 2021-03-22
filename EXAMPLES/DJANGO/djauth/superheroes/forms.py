#!/usr/bin/env python
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, strip=True, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'autofocus': 'autofocus', 'required': 'required',}) # 'placeholder': 'User Name'})
        self.fields['password'].widget.attrs.update({'required': 'required', }) #, 'placeholder': 'Password'})
