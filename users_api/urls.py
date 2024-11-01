from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users_api.apps import UsersApiConfig
from users_api.views import UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    UserListAPIView, UserPreferencesUpdateAPIView, UserPreferencesRetrieveAPIView, UserStatisticsRetrieveAPIView

app_name = UsersApiConfig.name

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='users_create'),
    path('', UserListAPIView.as_view(), name='users_list'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='users_detail'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='users_update'),
    path('delite/<int:pk>/', UserDestroyAPIView.as_view(), name='users_delite'),
    path('add_preferences/<int:pk>/', UserPreferencesUpdateAPIView.as_view(), name='add_preferences'),
    path('preferences/<int:pk>/', UserPreferencesRetrieveAPIView.as_view(), name='preferences'),
    path('statistics/<int:pk>/', UserStatisticsRetrieveAPIView.as_view(), name='statistics'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]