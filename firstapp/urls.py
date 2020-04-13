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
from firstapp.views.user import UserLoginView, UserLogoutView
from firstapp.views.todo_cls import (TodoListView, TodoDetailView,
                                     TodoCreateView, TodoUpdateView,
                                     TodoDeleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('debug/', include(debug_toolbar.urls)),
    path('todo/list/', TodoListView.as_view(), name='todo-list'),
    path('todo/create/', TodoCreateView.as_view(), name='todo-create'),
    path('todo/<str:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('todo/update/<str:pk>/', TodoUpdateView.as_view(), name='todo-update'),
    path('todo/delete/<str:pk>/', TodoDeleteView.as_view(), name='todo-delete'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
]
