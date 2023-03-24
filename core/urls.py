from django.contrib import admin
from django.urls import path, include


# Endpoints
urlpatterns = [
    path("admin/", admin.site.urls),
    path("API/", include('avez.urls')),
]
