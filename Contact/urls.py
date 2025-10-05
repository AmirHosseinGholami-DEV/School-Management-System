from django.urls import path
from . import views

urlpatterns = [
    # Contact App Url
    path("", views.ContactView.as_view(), name="Contact Page"),
]
