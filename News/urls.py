from django.urls import path, include
from . import views

urlpatterns = [
    # News Page
    path("", views.News_View.as_view(), name="News Page"),
]