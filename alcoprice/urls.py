from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
    path("polet/", admin.site.urls),
    path("", include("products.urls")),
]
