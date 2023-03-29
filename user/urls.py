from django.urls import path
from .views import LoginView, SignUpView, ProfileView, ProfileUpdateView, PasswordChangeView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views
app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('signup/', SignUpView.as_view(), name='sign_view'),
    path('profile/', ProfileView.as_view(), name='profile_view'),
    path('profile/<int:pk>', ProfileUpdateView.as_view(), name='profile_update_view'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
]