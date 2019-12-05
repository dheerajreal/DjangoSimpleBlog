from django import forms

from .models import Comment, ContactFormEntry


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"})
    )
    email = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"})
    )
    message = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control"})
    )

    class Meta:
        model = ContactFormEntry
        fields = ["name", "email", "message", ]


class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"})
    )
    email = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"})
    )
    comment = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control", "rows": "3"})
    )

    class Meta:
        model = Comment
        fields = ["name", "email", "comment", ]
