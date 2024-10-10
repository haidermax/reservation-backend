# Create the necessary directories and init files for the job_notifications app
mkdir models
mkdir serializers
mkdir views
mkdir tests
mkdir tests\job_notification

# Create __init__.py files with pre-filled imports for each directory
# models/__init__.py
$modelsInitContent = @"
from .job_notification import JobNotification
"@
New-Item -Path "models\__init__.py" -ItemType File -Force -Value $modelsInitContent

# serializers/__init__.py
$serializersInitContent = @"
from .job_notification_serializer import JobNotificationSerializer
"@
New-Item -Path "serializers\__init__.py" -ItemType File -Force -Value $serializersInitContent

# views/__init__.py
$viewsInitContent = @"
from .job_notification_view import JobNotificationViewSet
"@
New-Item -Path "views\__init__.py" -ItemType File -Force -Value $viewsInitContent

# tests/__init__.py
$testsInitContent = @"
"@
New-Item -Path "tests\__init__.py" -ItemType File -Force -Value $testsInitContent

# tests/job_notification/__init__.py
$jobNotificationTestsInitContent = @"
"@
New-Item -Path "tests\job_notification\__init__.py" -ItemType File -Force -Value $jobNotificationTestsInitContent

# Create the models/job_notification.py file
$jobNotificationModelContent = @"
from django.db import models
from base.models.abstract_mixin import AbstractMixin
from base.models.user import User  # Assuming User is used for job seeker reference
from job_postings.models.job_posting import JobPosting  # Assuming JobPosting is used for job reference

class JobNotification(AbstractMixin):
    """
    Represents a job notification sent to a job seeker related to a specific job posting.
    """
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='notifications')  # The job related to the notification
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_notifications')  # The job seeker receiving the notification
    notification_text = models.TextField()  # Text of the notification

    def __str__(self):
        return f"Notification for {self.job_seeker.full_name} - Job: {self.job.job_title}"
"@
New-Item -Path "models\job_notification.py" -ItemType File -Force -Value $jobNotificationModelContent

# Create the serializers/job_notification_serializer.py file
$jobNotificationSerializerContent = @"
from rest_framework import serializers
from job_notifications.models.job_notification import JobNotification

class JobNotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for the JobNotification model.
    """

    class Meta:
        model = JobNotification
        fields = [
            'id',
            'job',
            'job_seeker',
            'notification_text',
            'create_date',
            'update_date',
            'create_user',
            'update_user',
            'is_archived',
        ]
        read_only_fields = [
            'create_date',
            'update_date',
            'create_user',
            'update_user',
            'is_archived',
        ]
"@
New-Item -Path "serializers\job_notification_serializer.py" -ItemType File -Force -Value $jobNotificationSerializerContent

# Create the views/job_notification_view.py file
$jobNotificationViewContent = @"
from rest_framework import viewsets, permissions
from job_notifications.models.job_notification import JobNotification
from job_notifications.serializers.job_notification_serializer import JobNotificationSerializer

class JobNotificationViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting job notification instances.
    """
    queryset = JobNotification.objects.all()
    serializer_class = JobNotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the notification with the user who created it.
        """
        serializer.save(create_user=self.request.user)

    def perform_update(self, serializer):
        """
        Save the notification with the user who updated it.
        """
        serializer.save(update_user=self.request.user)
"@
New-Item -Path "views\job_notification_view.py" -ItemType File -Force -Value $jobNotificationViewContent

# Create the tests/job_notification/test_view.py file
$jobNotificationTestContent = @"
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from base.models.user import User
from job_postings.models.job_posting import JobPosting
from job_notifications.models.job_notification import JobNotification

class JobNotificationCRUDTests(APITestCase):
    """
    Test suite for the JobNotification model and viewset.
    """

    def setUp(self):
        # Create a superuser for authentication
        self.superuser = User.objects.create_superuser(
            email='admin@example.com',
            full_name='Admin User',
            password='adminpassword123',
            role='admin'
        )
        self.client.login(email='admin@example.com', password='adminpassword123')

        # Create a test job seeker and job posting
        self.job_seeker = User.objects.create_user(
            email='jobseeker@example.com',
            full_name='Job Seeker User',
            password='jobseekerpassword123',
            role='job_seeker'
        )

        self.job_posting = JobPosting.objects.create(
            service_provider=self.superuser,
            service_provider_type='hospital',
            job_title='Nurse',
            job_description='Looking for experienced nurse.',
            qualifications='Nursing Degree',
            salary=4000,
            job_location='Hospital A',
            job_status='open',
        )

        # Create a sample notification instance for testing
        self.notification = JobNotification.objects.create(
            job=self.job_posting,
            job_seeker=self.job_seeker,
            notification_text='A new nurse position has been posted.',
        )

        # URLs for job notification-related API actions
        self.notification_list_url = reverse('jobnotification-list')
        self.notification_detail_url = lambda pk: reverse('jobnotification-detail', kwargs={'pk': pk})

    def test_get_notification_list(self):
        response = self.client.get(self.notification_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_notification_detail(self):
        response = self.client.get(self.notification_detail_url(self.notification.pk))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_notification(self):
        data = {
            'job': self.job_posting.id,
            'job_seeker': self.job_seeker.id,
            'notification_text': 'This is a new job notification.',
        }
        response = self.client.post(self.notification_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobNotification.objects.count(), 2)

    def test_partial_update_notification(self):
        data = {'notification_text': 'Updated notification text.'}
        response = self.client.patch(self.notification_detail_url(self.notification.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_notification(self):
        response = self.client.delete(self.notification_detail_url(self.notification.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
"@
New-Item -Path "tests\job_notification\test_view.py" -ItemType File -Force -Value $jobNotificationTestContent

# Create the urls.py file for the job_notifications app
$jobNotificationUrlsContent = @"
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from job_notifications.views.job_notification_view import JobNotificationViewSet

router = DefaultRouter()
router.register(r'job-notifications', JobNotificationViewSet, basename='jobnotification')

urlpatterns = [
    path('', include(router.urls)),
]
"@
New-Item -Path "urls.py" -ItemType File -Force -Value $jobNotificationUrlsContent

Write-Output "All files for the job_notifications app have been created successfully!"
