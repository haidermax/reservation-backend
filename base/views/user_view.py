from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import action
from ..serializers import UserSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        """
        Assign different permissions based on the action being performed.
        Only admin users can delete users, others can only list, retrieve, and update.
        """
        if self.action in ['list', 'retrieve', 'update', 'partial_update']:
            return [permissions.IsAuthenticated()]
        if self.action == 'destroy':
            return [permissions.IsAdminUser()]
        return super().get_permissions()

    def perform_create(self, serializer):
        """
        Save the user who created the object.
        """
        serializer.save(create_user=self.request.user)

    def perform_update(self, serializer):
        """
        Save the user who updated the object.
        """
        serializer.save(update_user=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        """
        An additional action to get the authenticated user's profile.
        """
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
