from django.urls import path
from . import views

urlpatterns = [
    # Teacher List Url
    path("seven_one/", views.Teacher_Seven_One_List.as_view(), name="Seven One Teacher List"),
    path("seven_two/", views.Teacher_Seven_Two_List.as_view(), name="Seven Two Teacher List"),
    path("eight_one/", views.Teacher_Eight_One_List.as_view(), name="Eight One Teacher List"),
    path("eight_two/", views.Teacher_Eight_Two_List.as_view(), name="Eight Two Teacher List"),
    path("nine_one/", views.Teacher_Nine_One_List.as_view(), name="Nine One Teacher List"),
    path("nine_two/", views.Teacher_Nine_Two_List.as_view(), name="Nine Two Teacher List"),
    
]