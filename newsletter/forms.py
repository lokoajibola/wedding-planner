# newsletter/forms.py
from django import forms
from .models import NewsletterSubscriber

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Your email address',
                'class': 'form-control'
            })
        }