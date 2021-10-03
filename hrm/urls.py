
from django.urls import path
from .api import UserList #, CustomAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/users_list/', UserList.as_view()),
    path('api/users_list/<int:pk>/', UserList.as_view()),
    #path('api-token-auth/', CustomAuthToken.as_view())
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),

]