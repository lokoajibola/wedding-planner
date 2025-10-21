# gallery/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.GalleryView.as_view(), name='gallery'),
    path('event/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
]