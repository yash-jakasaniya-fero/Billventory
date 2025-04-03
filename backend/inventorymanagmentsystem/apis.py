from django.urls import include, path

app_name = "apis"

urlpatterns = [
    path("", include(("organization.urls", "organization"), namespace="organization")),
]
