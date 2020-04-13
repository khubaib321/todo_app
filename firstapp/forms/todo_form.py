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

        user = kwargs.pop('user', None)
        super().__init__(data=data, **kwargs)

        if user and user.is_superuser is False:
            self.fields.pop('assigned_user', None)
