# booking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookCallView.as_view(), name='book_call'),
    path('success/', views.BookingSuccessView.as_view(), name='booking_success'),
]