import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone

class AbstractMixin(models.Model):
    """
    Abstract mixin that provides the fields:
    - id: UUID primary key.
    - create_date: Date when the record was created.
    - update_date: Date when the record was last updated.
    - create_user: User who created the record.
    - update_user: User who last updated the record.
    - is_archived: Boolean flag indicating if the record is archived.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_date = models.DateTimeField(default=timezone.now, editable=False)
    update_date = models.DateTimeField(auto_now=True)
    create_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="created_%(class)s_records",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    update_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="updated_%(class)s_records",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    is_archived = models.BooleanField(default=False)

    class Meta:
        abstract = True
