"""djangoworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from hello.views import my_view
from hello.views import home_view
from todo.views import todo_view, add_todo_view, delete_todo, add_pog_view, delete_pog

urlpatterns = [
    path('', home_view),
    path('todo/', todo_view),
    path('addTodo/', add_todo_view),
    path('addPog/', add_pog_view),
    path('deleteTodo/<int:todo_id>/', delete_todo),
    path('deletepog/<int:pog_id>/', delete_pog),
    path('admin/', admin.site.urls),
    path('sayHello/', my_view)
]
