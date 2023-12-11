from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.apis import (
    RegisterAPI,
    LoginAPI,
    LogoutAPI,
)

app_name = 'auth'

urlpatterns = [
       path('register/',RegisterAPI.as_view(), name="register"),
       path('login/',LoginAPI.as_view(), name="login"),
       path('logout/', LogoutAPI.as_view(), name="logout"),
       path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
