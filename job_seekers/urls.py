from django.urls import path, include
from rest_framework.routers import DefaultRouter
from job_seekers.views.job_seeker_view import JobSeekerUserViewSet

router = DefaultRouter()
router.register(r'jobseekers', JobSeekerUserViewSet, basename='jobseekeruser')

urlpatterns = [
    path('', include(router.urls)),
]