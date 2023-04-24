from django.urls import path
from .views import UserRegisterAPIView, UserDetailAPIView


urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='user_register'),
    path('me/<int:pk>', UserDetailAPIView.as_view(), name='user_detail'),
]