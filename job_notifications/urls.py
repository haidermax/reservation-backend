from django.urls import path, include
from rest_framework.routers import DefaultRouter
from job_notifications.views.job_notification_view import JobNotificationViewSet

router = DefaultRouter()
router.register(r'job-notifications', JobNotificationViewSet, basename='jobnotification')

urlpatterns = [
    path('', include(router.urls)),
]