"""User login/logout class based views"""

from django.contrib.auth.views import LoginView, LogoutView


class UserLoginView(LoginView):
    """User login view class"""

    template_name = 'login.html'


class UserLogoutView(LogoutView):
    """User login view class"""

    template_name = 'list.html'
