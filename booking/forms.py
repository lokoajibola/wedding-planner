# booking/forms.py
from django import forms
from .models import ConsultationBooking
from django.core.validators import RegexValidator

class ConsultationBookingForm(forms.ModelForm):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    client_phone = forms.CharField(validators=[phone_regex])
    
    class Meta:
        model = ConsultationBooking
        fields = ['client_name', 'client_email', 'client_phone', 'event_type', 'event_date', 'preferred_date', 'message']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'preferred_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})