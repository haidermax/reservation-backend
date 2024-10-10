from django.db import models
from base.models.abstract_mixin import AbstractMixin
from base.models.user import User  # Assuming User is used for recipient reference

class Notification(AbstractMixin):
    """
    Represents a notification sent to a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')  # The user receiving the notification
    notification_text = models.TextField()
    is_read = models.BooleanField(default=False)  # Flag to indicate if the notification has been read

    def __str__(self):
        return f"Notification for {self.user.full_name}: {self.notification_text[:50]}"