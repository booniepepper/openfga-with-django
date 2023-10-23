from django.urls import path

from . import views

urlpatterns = [
    path("auth_models", views.auth_models, name="auth_models"),
]
