from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login/', views.login_user),
    path('register/', views.register_user),
    path('logout/', views.logout_user),
    path('todo/', views.todo_page),
    path('complete/<int:task_id>/', views.complete_task),
]