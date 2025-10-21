# core/views.py

from blog.models import BlogPost
from gallery.models import Event
from django.views.generic import CreateView, TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm
# core/views.py (add these)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from booking.models import ConsultationBooking
from .models import ContactMessage, Testimonial

# core/views.py (update HomeView)
class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_events'] = Event.objects.filter(is_featured=True).prefetch_related('images')[:6]
        context['recent_posts'] = BlogPost.objects.filter(is_published=True)[:3]
        context['testimonials'] = Testimonial.objects.filter(is_featured=True)[:4]
        return context

class ContactView(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact_success')
    
    def form_valid(self, form):
        messages.success(self.request, 'Thank you for your message! We will get back to you soon.')
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'contact/contact_success.html'
    

class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'admin/dashboard.html'
    
    def test_func(self):
        return self.request.user.is_admin()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_bookings'] = ConsultationBooking.objects.all().order_by('-created_at')[:5]
        context['total_events'] = Event.objects.count()
        context['total_messages'] = ContactMessage.objects.count()
        context['total_posts'] = BlogPost.objects.count()
        context['pending_bookings'] = ConsultationBooking.objects.filter(status='pending').count()
        return context

class EventManagementView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Event
    template_name = 'admin/event_management.html'
    context_object_name = 'events'
    
    def test_func(self):
        return self.request.user.is_admin()
    
    def get_queryset(self):
        return Event.objects.all().prefetch_related('images')

class TestimonialCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Testimonial
    fields = ['client_name', 'client_company', 'content', 'rating', 'is_featured']
    template_name = 'admin/testimonial_form.html'
    success_url = reverse_lazy('admin_dashboard')
    
    def test_func(self):
        return self.request.user.is_admin()