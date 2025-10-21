from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import AdminDashboardView, EventManagementView, TestimonialCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('dashboard/events/', EventManagementView.as_view(), name='event_management'),
    path('dashboard/testimonials/add/', TestimonialCreateView.as_view(), name='add_testimonial'),
    path('', include('core.urls')),
    path('gallery/', include('gallery.urls')),
    path('booking/', include('booking.urls')),
    path('blog/', include('blog.urls')),
    path('newsletter/', include('newsletter.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)