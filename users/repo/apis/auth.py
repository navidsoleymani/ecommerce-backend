from gando.architectures.apis import BaseAPI

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import TokenRefreshView


class HasLoginAPI(BaseAPI, TokenVerifyView):
    pass


class LoginAPI(BaseAPI, TokenObtainPairView):
    pass


class RefreshLoginAPI(BaseAPI, TokenRefreshView):
    pass
