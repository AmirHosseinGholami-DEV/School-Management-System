from django.urls import path
from . import views



urlpatterns = [
    # Student Url
    path('', views.Seven_One_Student.as_view(), name='management'),
    path('seven_student_two/', views.Seven_Two_Student.as_view(), name='Seven_Two_Student_Management'),
    path('eight_student_one/', views.Eight_One_Student.as_view(), name='Eight_One_Student_Management'),
    path('eight_student_two/', views.Eight_Two_Student.as_view(), name='Eight_Two_Student_Management'),
    path('nine_student_one/', views.Nine_One_Student.as_view(), name='Nine_One_Student_Management'),
    path('nine_student_two/', views.Nine_Two_Student.as_view(), name='Nine_Two_Student_Management'),

    # Teacher Url
    path('seven_teacher_one/', views.Seven_One_Teacher.as_view(), name='Seven_One_Teacher_Management'),
    path('seven_teacher_two/', views.Seven_Two_Teacher.as_view(), name='Seven_Two_Teacher_Management'),
    path('eight_teacher_one/', views.Eight_One_Teacher.as_view(), name='Eight_One_Teacher_Management'),
    path('eight_teacher_two/', views.Eight_Two_Teacher.as_view(), name='Eight_Two_Teacher_Management'),
    path('nine_teacher_one/', views.Nine_One_Teacher.as_view(), name='Nine_One_Teacher_Management'),
    path('nine_teacher_two/', views.Nine_Two_Teacher.as_view(), name='Nine_Two_Teacher_Management'),

    # Staff Url
    path('staff/', views.StaffList.as_view(), name='staff_Management'),

    # Absence Url
    path('seven_absence_one/', views.Seven_One_Absence.as_view(), name='Seven_One_Absence_Management'),
    path('seven_absence_two/', views.Seven_Two_Absence.as_view(), name='Seven_Two_Absence_Management'),
    path('eight_absence_one/', views.Eight_One_Absence.as_view(), name='Eight_One_Absence_Management'),
    path('eight_absence_two/', views.Eight_Two_Absence.as_view(), name='Eight_Two_Absence_Management'),
    path('nine_absence_one/', views.Nine_One_Absence.as_view(), name='Nine_One_Absence_Management'),
    path('nine_absence_two/', views.Nine_Two_Absence.as_view(), name='Nine_Two_Absence_Management'),
]
