"""Todo class based views"""

from django.views.generic import (CreateView, UpdateView, DeleteView,
                                  DetailView, ListView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from firstapp.forms import TodoForm
from firstapp.classes.todo import Todo


class AccessControlMixin(UserPassesTestMixin):
    """Access control mixin for model records"""

    def test_func(self):
        """Overriding UserPassesTestMixin.test_func
        Checks if a user is allowed to operate on a model record.

        :return: (bool) True if allowed, False otherwise
        """

        todo = self.get_object()
        return self.request.user.is_superuser or \
            self.request.user == todo.assigned_user


class TodoBaseView(LoginRequiredMixin):
    """Base class for todo views"""

    model = Todo
    form_class = TodoForm
    context_object_name = 'instance'


class TodoListView(TodoBaseView, ListView):
    """Todo list view class"""

    template_name = 'list.html'

    def get_queryset(self):
        """Overriding MultipleObjectMixin.get_queryset
        Filters only assigned records for non super users.

        :return: (QuerySet) filtered query set according to user permission
        """

        query_set = super().get_queryset()
        if not self.request.user.is_superuser:
            return query_set.filter(assigned_user=self.request.user).values(
                'pk', 'name')

        return query_set


class TodoCreateView(TodoBaseView, CreateView):
    """Todo create view class"""

    template_name = 'create_update.html'

    def get_form_kwargs(self):
        """Overriding ModelFormMixin.get_form_kwargs
        Adding current request user to to kwargs dictioanry.

        :return: (dict) dictionary of kwargs
        """

        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        """Overriding FormMixin.form_valid.
        Force assign record to current user if creating user is not
        a super user.

        :param form: (forms.ModelForm) model form object
        :return: (HttpResponseRedirect) redirection object
        """

        if not self.request.user.is_superuser:
            form.instance.assigned_user = self.request.user

        return super().form_valid(form)


class TodoDetailView(AccessControlMixin, TodoBaseView, DetailView):
    """Todo detail view class"""

    template_name = 'detail.html'


class TodoUpdateView(AccessControlMixin, TodoCreateView, UpdateView):
    """Todo update view class"""


class TodoDeleteView(AccessControlMixin, TodoBaseView, DeleteView):
    """Todo delete view class"""

    success_url = '/todo/show/'
    template_name = 'delete.html'
