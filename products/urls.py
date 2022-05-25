from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
    path("", views.OverviewView.as_view()),
    path("table", views.TableView.as_view()),
]
