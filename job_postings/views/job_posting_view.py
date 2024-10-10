from rest_framework import viewsets, permissions
from job_postings.models.job_posting import JobPosting
from job_postings.serializers.job_posting_serializer import JobPostingSerializer

class JobPostingViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting job posting instances.
    """
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the job posting with the user who created it.
        """
        serializer.save(create_user=self.request.user)

    def perform_update(self, serializer):
        """
        Save the job posting with the user who updated it.
        """
        serializer.save(update_user=self.request.user)