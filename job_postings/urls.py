from django.urls import path, include
from rest_framework.routers import DefaultRouter
from job_postings.views.job_posting_view import JobPostingViewSet

router = DefaultRouter()
router.register(r'job-postings', JobPostingViewSet, basename='jobposting')

urlpatterns = [
    path('', include(router.urls)),
]