"""firstapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from firstapp.views import todo, user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('debug/', include(debug_toolbar.urls)),
    path('home', todo.list, name='home'),
    path('todo/show/', todo.list, name='todo-show'),
    path('todo/create/', todo.create, name='todo-create'),
    path('todo/update/<str:id>/', todo.update, name='todo-update'),
    path('todo/delete/<str:id>/', todo.delete, name='todo-delete'),
    path('login/', LoginView.as_view(template_name='login.html'), name='user-login'),
    path('logout/', user.log_out, name='user-logout'),
]
