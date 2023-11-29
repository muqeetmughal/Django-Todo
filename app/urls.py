from django.urls import path, include
from app import views

urlpatterns = [
    path('',views.home, name = 'home' ),
    path('task',views.task, name = 'task' ),
    path('todo',views.todo, name = 'todo' ),

]
