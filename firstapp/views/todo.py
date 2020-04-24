"""Todo app views. Obsolete now since using Class based views in todo_cls.py"""

from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from firstapp.forms import TodoForm


def _validate_permissions(request, todo=None):
    """Check if permissions are valid for a user and record.
    Only allow users to update/delete their assigned records.
    Only logged in users can perform operations.

    :param request: (HttpRequest) request object
    :param model_obj: (Todo) todo model
    :raises PermissionError: raises Error if not permitted
    :return: (bool) True if valid
    """

    if not request.user.is_authenticated or (
       todo and (request.user.id != todo.assigned_user_id) and not request.user.is_superuser):
        raise PermissionError('You do not have permission for this operation.')

    return True


def create(request):
    """Handle form create requests"""

    context = {
        'form': None
    }

    try:
        _validate_permissions(request)
        if request.method == 'POST':
            todo_form = TodoForm(request.POST, user=request.user)

            if not todo_form.is_valid():
                raise ValidationError('Invalid form data.')

            todo_form.save()
            messages.success(request, 'Todo created.')

    except PermissionError as exception:
        messages.error(request, str(exception))
        return redirect('todo-show')

    except Exception as exception:
        messages.error(request, str(exception))

    context['form'] = TodoForm(user=request.user)
    return render(request, 'create_update.html', context=context)


def update(request, id):
    """Handle form update requests"""

    context = {
        'form': None
    }

    try:
        todo = TodoForm.Meta.model.objects.filter(id=id).first()
        _validate_permissions(request, todo)

        if request.method == 'POST':
            todo_form = TodoForm(request.POST, instance=todo, user=request.user)

            if not todo_form.is_valid():
                raise ValidationError('Invalid form data.')

            todo_form.save()
            messages.success(request, 'Todo updated.')

    except PermissionError as exception:
        messages.error(request, str(exception))
        return redirect('todo-show')

    except Exception as exception:
        messages.error(request, str(exception))

    context['form'] = TodoForm(instance=todo, user=request.user)
    return render(request, 'create_update.html', context=context)


def delete(request, id):
    """Handles delete requests"""

    try:
        todo = TodoForm.Meta.model.objects.filter(id=id).first()
        _validate_permissions(request, todo)
        todo.delete()

    except Exception as exception:
        messages.error(request, str(exception))

    return redirect('todo-show')


def list(request):
    """Handle list/detail requests"""

    context = {
        'todos': None
    }
    try:
        if request.user.is_superuser:
            context['todos'] = TodoForm.Meta.model.objects.all() \
                .values('id', 'name')
        else:
            context['todos'] = TodoForm.Meta.model.objects.filter(
                assigned_user_id=request.user.id).values('id', 'name')

    except Exception as exception:
        messages.error(request, str(exception))

    return render(request, 'list.html', context=context)
