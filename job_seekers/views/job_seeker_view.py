from rest_framework import viewsets, permissions
from job_seekers.models.job_seeker_user import JobSeekerUser
from job_seekers.serializers.job_seeker_serializer import JobSeekerUserSerializer

class JobSeekerUserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing, creating, updating, and deleting job seeker instances.
    """
    queryset = JobSeekerUser.objects.all()
    serializer_class = JobSeekerUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Save the job seeker instance with the current user as the creator.
        """
        serializer.save(create_user=self.request.user)

    def perform_update(self, serializer):
        """
        Save the job seeker instance with the current user as the updater.
        """
        serializer.save(update_user=self.request.user)