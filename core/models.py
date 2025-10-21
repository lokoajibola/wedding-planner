# core/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('client', 'Client'),
    )
    role = models.CharField(max_length=20, choices=USER_ROLES, default='client')
    phone_number = models.CharField(max_length=15, blank=True)
    company_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

    def is_admin(self):
        return self.role == 'admin'
    
# core/models.py (add this to existing file)
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_responded = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Message from {self.name}"

# core/models.py (add this)
class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Testimonial - {self.client_name}"
    
    def stars(self):
        return '★' * self.rating + '☆' * (5 - self.rating)