# gallery/views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Event, EventCategory

class GalleryView(ListView):
    model = Event
    template_name = 'gallery/gallery.html'
    context_object_name = 'events'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Event.objects.prefetch_related('images').all()
        
        # Filter by category if provided
        category_slug = self.request.GET.get('category')
        if category_slug:
            queryset = queryset.filter(category__name__iexact=category_slug)
            
        # Filter by event type if provided
        event_type = self.request.GET.get('type')
        if event_type:
            queryset = queryset.filter(event_type=event_type)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = EventCategory.objects.all()
        context['event_types'] = Event.EVENT_TYPES
        return context

class EventDetailView(DetailView):
    model = Event
    template_name = 'gallery/event_detail.html'
    context_object_name = 'event'