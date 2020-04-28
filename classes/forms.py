from django import forms

class Email_form(forms.Form):
    """Form to be used to send emails"""
    your_name = forms.CharField(label='Your name', max_length=100)
    your_email = forms.CharField(label='Your email', max_length=100)
    your_request = forms.CharField(label='Your request', widget=forms.Textarea)
    
    