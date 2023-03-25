from django.urls import path
from accounts.views import LoginView, logout_view, RegisterView, UpdatePassword, UserDetailView, UserUpdateView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password_update/', UpdatePassword.as_view(), name='password_update'),
    path('user_detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
]
