from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Staff_View.as_view(), name="Staff Page"),
]
