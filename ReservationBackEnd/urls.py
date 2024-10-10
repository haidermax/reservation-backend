from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('doctors.urls')),
    path('', include('clinics.urls')),
    path('', include('job_seekers.urls')),
    path('', include('offers.urls')),
    path('', include('reservations.urls')),
    path('', include('notifications.urls')),
    path('', include('appointments.urls')),
    path('', include('reviews.urls')),
    path('', include('message.urls')),
    path('', include('job_postings.urls')),
    path('', include('applications.urls')),
    path('', include('job_notifications.urls')),
]
