from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import logout


def log_out(request):
    """Handles user log out requests"""

    try:
        logout(request)
        messages.success(request, 'Log out successful.')

    except Exception as exception:
        messages.error(request, str(exception))

    finally:
        return redirect('home')
