# gallery/models.py
from django.db import models
from django.conf import settings
from .utils import compress_image


class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    EVENT_TYPES = (
        ('wedding', 'Wedding'),
        ('corporate', 'Corporate Event'),
        ('birthday', 'Birthday'),
        ('anniversary', 'Anniversary'),
        ('other', 'Other'),
    )
    
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    description = models.TextField()
    event_date = models.DateField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='event_images/')
    caption = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    display_order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['display_order', 'uploaded_at']
    
    def save(self, *args, **kwargs):
        # Compress image before saving
        if self.image:
            self.image = compress_image(self.image)
        super().save(*args, **kwargs)