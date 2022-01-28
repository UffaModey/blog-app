from django import forms

class Emails(forms.Form):
    email = forms.CharField(label='email', max_length=200)
    emailn = forms.CharField(label='emailn', max_length=200)