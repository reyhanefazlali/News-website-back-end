from email import message
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'