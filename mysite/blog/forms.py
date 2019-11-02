from django import forms
from .models import ContactFormEntry


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = ContactFormEntry
        fields = ["name", "email", "message", ]
    
