from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authentication.views import (
    EmailTokenObtainPairViewSet,
    UserRegistrationViewSet,
    UsersListViewSet
)


urlpatterns = [
    path('token/', EmailTokenObtainPairViewSet.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationViewSet.as_view({'post': 'create'}), name='register'),
    path('users/', UsersListViewSet.as_view({'get': 'list'}), name='users'),
]
