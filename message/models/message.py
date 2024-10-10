from django.db import models
from base.models.abstract_mixin import AbstractMixin
from base.models.user import User  # Assuming User is used for sender and receiver references

class Message(AbstractMixin):
    """
    Represents a message between two users.
    """
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message_text = models.TextField()
    message_image = models.CharField(max_length=255, null=True, blank=True)  # Optional message image

    def __str__(self):
        return f"Message from {self.sender.full_name} to {self.receiver.full_name}"