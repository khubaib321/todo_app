"""Todo form"""

from django import forms
from firstapp.classes.todo import Todo


class TodoForm(forms.ModelForm):
    """Todo form class"""

    short_desc = forms.CharField(max_length=255, required=False,
                                 widget=forms.Textarea,
                                 label='Short description')

    class Meta:
        """Meta class for todo form"""

        model = Todo
        fields = ['name', 'reminder', 'short_desc', 'assigned_user']

    def __init__(self, data=None, **kwargs):
        """Removes assigned user field for non superusers.

        :param data: (dict), data dictionary defaults to None
        """

        self._user = kwargs.pop('user', None)
        super().__init__(data=data, **kwargs)

        if self._user and not self._user.is_superuser:
            self.fields.pop('assigned_user', None)

    def save(self, commit=True):
        """Overriding BaseModelForm.save
        Set assigned user before saving form

        :param commit: (bool) True if save immediately
        :return: (Todo) model instance
        """

        self.instance.set_assigned_user(self._user)
        return super(TodoForm, self).save(commit)
