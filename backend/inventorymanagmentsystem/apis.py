from django.urls import include, path

app_name = "apis"

urlpatterns = [
    path("org/", include(("organization.urls", "organization"), namespace="organization")),
    path("auth/", include(("authentication.urls", "authentication"), namespace="authentication")),
]
