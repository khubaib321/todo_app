"""Todo"""

from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    """Todo model"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=32)
    reminder = models.BooleanField(default=False)
    short_desc = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        """Get str value for class objects"""

        return self.name

    def set_assigned_user(self, request):
        """Assign currently logged in user to model object

        :param request: (HttpRequest) Http request object
        """

        request_user = getattr(request, 'user', None)
        if (request_user and request_user.is_superuser) or not request_user.is_authenticated:
            # Do not force assignment if superuser, let them assign to anyone
            return

        self.assigned_user = request_user
