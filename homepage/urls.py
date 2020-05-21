from django.urls import path

from homepage import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
