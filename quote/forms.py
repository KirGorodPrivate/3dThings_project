from django import forms

from .models import Quote

# class QuoteForm(forms.Form):
#     class Meta:
#         model = Quote
#         fields = ('username', 'email', 'phone', 'description', 'deadline', 'document')

# class QuoteForm(forms.Form):
#     username = forms.TextInput()
#     email = forms.TextInput()
#     phone = forms.TextInput()
#     description = forms.TextInput()
#     deadline = forms.TextInput()
#     document = forms.FileInput()

class QuoteForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
       "class": "form-control" 
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    deadline = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control"
    }))
    document = forms.FileField()