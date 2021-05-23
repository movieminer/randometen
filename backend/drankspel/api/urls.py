from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("", include([path("v1/", include("drankspel.api.v1.urls", namespace="v1")),]),),  # noqa
    path(
        "docs",
        TemplateView.as_view(template_name="drankspel/swagger.html", extra_context={"schema_urls": ["v1:schema-v1"]},),
        name="swagger",
    ),
    path(
        "docs/oauth2-redirect",
        TemplateView.as_view(template_name="drankspel/swagger-oauth2-redirect.html"),
        name="swagger-oauth-redirect",
    ),
]
