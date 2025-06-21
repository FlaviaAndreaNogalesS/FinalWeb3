from django.urls import path
from users.views.auth_view import LoginView
from users.views.user_view import UserListCreateView, UserDetailView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:id>/', UserDetailView.as_view()),
]
