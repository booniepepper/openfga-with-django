from django.urls import path

from . import views

urlpatterns = [
    path("sync/auth_models", views.auth_models_sync, name="auth_models_sync"),
    path("async/auth_models", views.auth_models, name="auth_models"),
]
