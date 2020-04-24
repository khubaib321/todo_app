"""Model serializers"""

from django.contrib.auth.models import User
from firstapp.classes.todo import Todo
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User model serializer"""

    class Meta:
        """Meta class for serializer"""

        model = User
        fields = ['url', 'username', 'email']


class TodoSerializer(serializers.ModelSerializer):
    """Todo model serializer"""

    class Meta:
        """Meta class for serializer"""

        model = Todo
        fields = ['url', 'name', 'reminder', 'short_desc', 'assigned_user']

    def _get_request_user(self):
        """Get user set in request.

        :return: (User) user model instance
        """

        request = self._context.get('request', None)
        return getattr(request, 'user', None)

    def to_representation(self, instance):
        """Overriding Serializer.to_representation
        Removes assigned_user field for non superusers.

        :param instance: (Todo) todo model
        :return: (dict) serialized model
        """

        request_user = self._get_request_user()
        representation = super(TodoSerializer, self).to_representation(instance)
        if request_user and not request_user.is_superuser:
            representation.pop('assigned_user')

        return representation

    def save(self, **kwargs):
        """Overriding BaseSerializer.save
        Forces assigned user to request user for non super users.

        :param kwargs: (dict) keyword arguments
        :return: (Todo) todo model instance
        """

        request_user = self._get_request_user()
        if request_user and not request_user.is_superuser:
            kwargs['assigned_user'] = request_user

        return super(TodoSerializer, self).save(**kwargs)
