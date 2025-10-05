from django.urls import path, include
from . import views

urlpatterns = [
    # Home Page
    path("", views.HomeView.as_view(), name="Home Page"),

    # Teacher App Url
    path("teacher/", include("TeacherList.urls"), name="Teacher List"),

    # Student App Url
    path("student/", include("StudentList.urls"), name="Student List"),

    # News App Url
    path("news/", include("News.urls"), name="News Page"),

    # Contact App Url
    path("contact/", include("Contact.urls"), name="Contact Page"),

    # Staff App Url
    path("staff/", include("Staff.urls"), name="Staff Page"),

    # About App Url
    path("about/", views.AboutView.as_view(), name="About Page"),
]
