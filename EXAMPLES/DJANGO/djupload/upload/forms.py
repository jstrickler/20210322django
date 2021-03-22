from django import forms

from upload.models import Document


class DocForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
