from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="Big-Prize API",
        default_version="v1",
        description="The Digikala Big-Prize campaign marketing product API document.",
        contact=openapi.Contact(email="r.shahnazar@digikala.com"),
    ),
    public=True,
    authentication_classes=(SessionAuthentication,),
    permission_classes=(AllowAny,),
)
