# booking/models.py
from django.db import models

class ConsultationBooking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    
    EVENT_TYPES = (
        ('wedding', 'Wedding'),
        ('corporate', 'Corporate Event'),
        ('birthday', 'Birthday'),
        ('anniversary', 'Anniversary'),
        ('other', 'Other'),
    )
    
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    client_phone = models.CharField(max_length=15)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    event_date = models.DateField()
    message = models.TextField(blank=True)
    preferred_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Consultation - {self.client_name}"