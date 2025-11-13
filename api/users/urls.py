from django.urls import path
from .views import UserCreateView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'users'
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserCreateView.as_view(), name='user-create'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]
