from django.urls import path
from config.repo.swagger.v1.schema import schema_view

app_name = "Swagger API Document Version 1"

urlpatterns = [
    path(
        "docs<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
