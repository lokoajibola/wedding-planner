# gallery/admin.py
from django.contrib import admin
from .models import EventCategory, Event, EventImage

class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'event_date', 'is_featured', 'created_by']
    list_filter = ['event_type', 'is_featured', 'event_date']
    search_fields = ['title', 'description']
    inlines = [EventImageInline]
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']

admin.site.register(EventImage)