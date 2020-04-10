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

    def __init__(self, data=None, request=None, **kwargs):
        super().__init__(data=data, **kwargs)

        # Hide assigned user field for non superusers
        if request and not request.user.is_superuser:
            self.fields['assigned_user'].widget = self.fields['assigned_user'].hidden_widget()
