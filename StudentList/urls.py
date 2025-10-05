from django.urls import path, include
from . import views

urlpatterns = [
    # Student List Url
    path("seven_one/", views.Student_Seven_One_List.as_view(), name="Seven One Student List"),
    path("seven_two/", views.Student_Seven_Two_List.as_view(), name="Seven Two Student List"),
    path("eight_one/", views.Student_Eight_One_List.as_view(), name="Eight One Student List"),
    path("eight_two/", views.Student_Eight_Two_List.as_view(), name="Eight Two Student List"),
    path("nine_one/", views.Student_Nine_One_List.as_view(), name="Nine One Student List"),
    path("nine_two/", views.Student_Nine_Two_List.as_view(), name="Nine Two Student List"),
]
