from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
            'class': 'custom-input',
            'placeholder': 'Your full name'
        }))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'custom-input', 
            'placeholder': 'your.email@example.com'
        }))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'custom-textarea', 'placeholder': 'Enter your message here...'}
    ))