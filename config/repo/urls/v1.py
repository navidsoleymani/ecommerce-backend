from django.urls import path, include

app_name = 'apiVersion1'

urlpatterns = [
    path('auth/', include('users.auth_urls')),
    path('users/', include('users.urls')),
]
