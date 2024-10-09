from django.urls import path

from . import views

app_name = 'supertodo'

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/<ToDoItem_slug>/', views.todo_detail, name='todo_detail'),
]
