"""Todo"""

from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Todo(models.Model):
    """Todo model"""

    id = models.AutoField(primary_key=True, auto_created=True, serialize=False)
    name = models.CharField(max_length=32)
    reminder = models.BooleanField(default=False)
    short_desc = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    assigned_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)

    def __str__(self):
        """Get str value for class objects"""

        return self.name

    def set_assigned_user(self, request_user):
        """Method obsolete after using Class based views.
        Assign currently logged in user to model object.

        :param request_user: (User) user model
        """

        if getattr(request_user, 'is_superuser'):
            # Do not force assignment if superuser, let them assign to anyone
            return

        self.assigned_user = request_user

    def get_absolute_url(self):
        """Overriding ModelBase.get_absolute_url
        Get absolute url for a record of this model

        :return: (str) absolute url to a model record
        """

        return reverse('todo-detail', kwargs={'pk': self.pk})
