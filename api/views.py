"""API view sets"""

from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from firstapp.classes.todo import Todo
from api.serializers import UserSerializer, TodoSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Todos to be viewed and deleted.
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Overriding GenericAPIView.get_queryset
        Filters only assigned records for non super users.

        :return: (QuerySet) filtered query set according to user assigned
        """

        query_set = super().get_queryset()
        if self.request.user.is_superuser is False:
            return query_set.filter(assigned_user=self.request.user).all()

        return query_set
