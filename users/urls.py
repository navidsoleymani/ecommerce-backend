from django.urls import path, include

app_name = 'users'

urlpatterns = [
    path('profiles/', include('users.repo.urls.user')),
]
