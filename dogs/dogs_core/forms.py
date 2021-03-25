from django import forms
from .models import Dog, Breed

class DogAddForm(forms.ModelForm):
    class Meta:
        model = Dog
        exclude = []
        # or
        # fields = ['name', 'breed']

class OtherForm(forms.Form):
    dog_name = forms.CharField(label='Name', widget=forms.TextInput(attrs={"class": "name"}), required=False)
    dog_breed = forms.ModelChoiceField(
        queryset=Breed.objects.all(),
        label='Breed',
        widget=forms.TextInput(attrs={"class": "breed"}),
        required=False
    )
    dog_sex = forms.ChoiceField(label='Sex', choices=Dog.SEX_CHOICES, required=False)
    dog_is_neutered = forms.BooleanField(label='Is neutered?', required=False)