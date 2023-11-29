from django.urls import path

from users.apis import (
    GetMyProfileInformationAPI,
)

app_name = 'users'
urlpatterns = [
    path('me/', GetMyProfileInformationAPI.as_view(), name='myProfile'),
]
