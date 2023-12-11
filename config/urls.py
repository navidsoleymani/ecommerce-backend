from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config.settings import (
    ADMIN_URL,
    PROJECT_NAME_URL_PARAM,
    ADMIN_INDEX_TITLE,
    ADMIN_SITE_HEADER,
    ADMIN_SITE_TITLE,
    STATIC_URL,
    STATIC_ROOT,
    MEDIA_URL,
    MEDIA_ROOT,
)

urlpatterns = (
        [
            path(ADMIN_URL, admin.site.urls),
            path(
                "apidoc/v1/" + PROJECT_NAME_URL_PARAM + "/",
                include("config.repo.swagger.v1.urls"),
            ),
            path("api/v1/" + PROJECT_NAME_URL_PARAM + "/", include("config.repo.urls.v1")),
            path('products/', include('product.urls')),
        ]
        + static(STATIC_URL, document_root=STATIC_ROOT)
        + static(MEDIA_URL, document_root=MEDIA_ROOT)
)

admin.site.site_header = ADMIN_SITE_HEADER
admin.site.site_title = ADMIN_SITE_TITLE
admin.site.index_title = ADMIN_INDEX_TITLE
