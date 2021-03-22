from django import forms

# Create your forms here.

class SimpleForm(forms.Form):
    user_name = forms.CharField(max_length=32)

