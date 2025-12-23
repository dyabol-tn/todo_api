from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path('tasks', TaskList.as_view()),
    path('tasks/<int:id>', TaskDetail.as_view()),
]