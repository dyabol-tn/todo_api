from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import TaskList, TaskDetail, RegisterView, UserDetailView

urlpatterns = [
    path('tasks', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>', TaskDetail.as_view(), name='task-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('profile/', UserDetailView.as_view(), name='profile'),
]