# booking/views.py
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ConsultationBooking
from .forms import ConsultationBookingForm

class BookCallView(CreateView):
    model = ConsultationBooking
    form_class = ConsultationBookingForm
    template_name = 'booking/book_call.html'
    success_url = reverse_lazy('booking_success')
    
    def form_valid(self, form):
        messages.success(self.request, 'Your consultation request has been submitted successfully! We will contact you soon.')
        return super().form_valid(form)

class BookingSuccessView(TemplateView):
    template_name = 'booking/booking_success.html'