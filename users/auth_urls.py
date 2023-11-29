from django.urls import path

from users.apis import (
    LoginAPI,
    HasLoginAPI,
    RefreshLoginAPI,
)

app_name = 'auth'
urlpatterns = [
    path('login/', LoginAPI.as_view(), name='login'),
    path('login/refresh/', RefreshLoginAPI.as_view(), name='refreshLogin'),
    path('login/try/', HasLoginAPI.as_view(), name='hasLogin'),
]
