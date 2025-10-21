# newsletter/views.py
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import NewsletterSubscriber
from .forms import NewsletterSubscriptionForm

class NewsletterSubscribeView(CreateView):
    model = NewsletterSubscriber
    form_class = NewsletterSubscriptionForm
    success_url = reverse_lazy('newsletter_success')
    
    def form_valid(self, form):
        messages.success(self.request, 'Thank you for subscribing to our newsletter!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # Handle duplicate email gracefully
        if 'email' in form.errors:
            messages.info(self.request, 'This email is already subscribed to our newsletter.')
        return super().form_invalid(form)

class NewsletterSuccessView(TemplateView):
    template_name = 'newsletter/subscription_success.html'