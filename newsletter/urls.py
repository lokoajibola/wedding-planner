# newsletter/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.NewsletterSubscribeView.as_view(), name='newsletter_subscribe'),
    path('success/', views.NewsletterSuccessView.as_view(), name='newsletter_success'),
]