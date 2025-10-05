from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.Admin_Panel_Seven_One.as_view(), name="admin"),

    # ====================================================================
    
    # Admin Dashboard Student:
    path('admin_dashboard_student/', views.Admin_Panel_Seven_One.as_view(), name='admin_dashboard'),
    path('admin_dashboard_student_seven_two/', views.Admin_Panel_Seven_Two.as_view(), name='admin_dashboard_seven_two'),
    path('admin_dashboard_student_eight_one/', views.Admin_Panel_Eight_One.as_view(), name='admin_dashboard_eight_one'),
    path('admin_dashboard_student_eight_two/', views.Admin_Panel_Eight_Two.as_view(), name='admin_dashboard_eight_two'),
    path('admin_dashboard_student_nine_one/', views.Admin_Panel_Nine_One.as_view(), name='admin_dashboard_nine_one'),
    path('admin_dashboard_student_nine_two/', views.Admin_Panel_Nine_Two.as_view(), name='admin_dashboard_nine_two'),
    
    # Add Student
    path('admin_dashboard_student_add/', views.Add_Student.as_view(), name='Add Student'),
    path('admin_dashboard_student_seven_one_add/', views.Add_Student_Seven_One.as_view(), name='Add Student Seven One'),
    path('admin_dashboard_student_seven_two_add/', views.Add_Student_Seven_Two.as_view(), name='Add Student Seven Two'),
    path('admin_dashboard_student_eight_one_add/', views.Add_Student_Eight_One.as_view(), name='Add Student Eight One'),
    path('admin_dashboard_student_eight_two_add/', views.Add_Student_Eight_Two.as_view(), name='Add Student Eight Two'),
    path('admin_dashboard_student_nine_one_add/', views.Add_Student_Nine_One.as_view(), name='Add Student Nine One'),
    path('admin_dashboard_student_nine_two_add/', views.Add_Student_Nine_Two.as_view(), name='Add Student Nine Two'),
    
    # Delete Admin Dashboard Student
    path('delete_student_student_seven_one/<int:pk>/', views.Delete_Student_Seven_One.as_view(), name='delete_student_seven_one'),
    path('delete_dashboard_student_seven_two/<int:pk>/', views.Delete_Student_Seven_Two.as_view(), name='delete_student_seven_two'),
    path('delete_dashboard_student_eight_one/<int:pk>/', views.Delete_Student_Eight_One.as_view(), name='delete_student_eight_one'),
    path('delete_dashboard_student_eight_two/<int:pk>/', views.Delete_Student_Eight_Two.as_view(), name='delete_student_eight_two'),
    path('delete_dashboard_student_nine_one/<int:pk>/', views.Delete_Student_Nine_One.as_view(), name='delete_student_nine_one'),
    path('delete_dashboard_student_nine_two/<int:pk>/', views.Delete_Student_Nine_Two.as_view(), name='delete_student_nine_two'),

    # Update Student
    path('update_student_seven_one/<int:pk>/', views.Update_Student_Seven_One.as_view(), name='update_student_seven_one'),
    path('update_student_seven_two/<int:pk>/', views.Update_Student_Seven_Two.as_view(), name='update_student_seven_two'),
    path('update_student_eight_one/<int:pk>/', views.Update_Student_Eight_One.as_view(), name='update_student_eight_one'),
    path('update_student_eight_two/<int:pk>/', views.Update_Student_Eight_Two.as_view(), name='update_student_eight_two'),
    path('update_student_nine_one/<int:pk>/', views.Update_Student_Nine_One.as_view(), name='update_student_nine_one'),
    path('update_student_nine_two/<int:pk>/', views.Update_Student_Nine_Two.as_view(), name='update_student_nine_two'),

    
    # ====================================================================


    # ====================================================================
    
    # Admin Dashboard Teacher:
    path('admin_dashboard_teacher_seven_one/', views.Admin_Panel_Teacher_Seven_One.as_view(), name='admin_dashboard_teacher_seven_one'),
    path('admin_dashboard_teacher_seven_two/', views.Admin_Panel_Teacher_Seven_Two.as_view(), name='admin_dashboard_teacher_seven_two'),
    path('admin_dashboard_teacher_eight_one/', views.Admin_Panel_Teacher_Eight_One.as_view(), name='admin_dashboard_teacher_eight_one'),
    path('admin_dashboard_teacher_eight_two/', views.Admin_Panel_Teacher_Eight_Two.as_view(), name='admin_dashboard_teacher_eight_two'),
    path('admin_dashboard_teacher_nine_one/', views.Admin_Panel_Teacher_Nine_One.as_view(), name='admin_dashboard_teacher_nine_one'),
    path('admin_dashboard_teacher_nine_two/', views.Admin_Panel_Teacher_Nine_Two.as_view(), name='admin_dashboard_teacher_nine_two'),
    
    # Add Teacher
    path('admin_dashboard_teacher_add/', views.Add_Teacher.as_view(), name='Add Teacher'),
    path('admin_dashboard_teacher_seven_one_add/', views.Add_Teacher_Seven_One.as_view(), name='Add Teacher Seven One'),
    path('admin_dashboard_teacher_seven_two_add/', views.Add_Teacher_Seven_Two.as_view(), name='Add Teacher Seven Two'),
    path('admin_dashboard_teacher_eight_one_add/', views.Add_Teacher_Eight_One.as_view(), name='Add Teacher Eight One'),
    path('admin_dashboard_teacher_eight_two_add/', views.Add_Teacher_Eight_Two.as_view(), name='Add Teacher Eight Two'),
    path('admin_dashboard_teacher_nine_one_add/', views.Add_Teacher_Nine_One.as_view(), name='Add Teacher Nine One'),
    path('admin_dashboard_teacher_nine_two_add/', views.Add_Teacher_Nine_Two.as_view(), name='Add Teacher Nine Two'),
    
    # Delete Admin Dashboard Teacher
    path('delete_teacher_seven_one/<int:pk>/', views.Delete_Teacher_Seven_One.as_view(), name='delete_teacher_seven_one'),
    path('delete_dashboard_teacher_seven_two/<int:pk>/', views.Delete_Teacher_Seven_Two.as_view(), name='delete_teacher_seven_two'),
    path('delete_dashboard_teacher_eight_one/<int:pk>/', views.Delete_Teacher_Eight_One.as_view(), name='delete_teacher_eight_one'),
    path('delete_dashboard_teacher_eight_two/<int:pk>/', views.Delete_Teacher_Eight_Two.as_view(), name='delete_teacher_eight_two'),
    path('delete_dashboard_teacher_nine_one/<int:pk>/', views.Delete_Teacher_Nine_One.as_view(), name='delete_teacher_nine_one'),
    path('delete_dashboard_teacher_nine_two/<int:pk>/', views.Delete_Teacher_Nine_Two.as_view(), name='delete_teacher_nine_two'),

    # Update Admin Teacher
    path('update_teacher_seven_one/<int:pk>/', views.Update_Teacher_Seven_One.as_view(), name='update_teacher_seven_one'),
    path('update_dashboard_teacher_seven_two/<int:pk>/', views.Update_Teacher_Seven_Two.as_view(), name='update_teacher_seven_two'),
    path('update_dashboard_teacher_eight_one/<int:pk>/', views.Update_Teacher_Eight_One.as_view(), name='update_teacher_eight_one'),
    path('update_dashboard_teacher_eight_two/<int:pk>/', views.Update_Teacher_Eight_Two.as_view(), name='update_teacher_eight_two'),
    path('update_dashboard_teacher_nine_one/<int:pk>/', views.Update_Teacher_Nine_One.as_view(), name='update_teacher_nine_one'),
    path('update_dashboard_teacher_nine_two/<int:pk>/', views.Update_Teacher_Nine_Two.as_view(), name='update_teacher_nine_two'),

    # ====================================================================


    # ====================================================================

    # Admin Dashboard Absent:
    path('admin_dashboard_absence_seven_one/', views.Admin_Panel_Absence_Seven_One.as_view(), name='admin_dashboard_absence_seven_one'),
    path('admin_dashboard_absence_seven_two/', views.Admin_Panel_Absence_Seven_Two.as_view(), name='admin_dashboard_absence_seven_two'),
    path('admin_dashboard_absence_eight_one/', views.Admin_Panel_Absence_Eight_One.as_view(), name='admin_dashboard_absence_eight_one'),
    path('admin_dashboard_absence_eight_two/', views.Admin_Panel_Absence_Eight_Two.as_view(), name='admin_dashboard_absence_eight_two'),
    path('admin_dashboard_absence_nine_one/', views.Admin_Panel_Absence_Nine_One.as_view(), name='admin_dashboard_absence_nine_one'),
    path('admin_dashboard_absence_nine_two/', views.Admin_Panel_Absence_Nine_Two.as_view(), name='admin_dashboard_absence_nine_two'),

    # Delete Admin Dashboard Absent
    path('delete_absence_seven_one/<int:pk>/', views.Delete_Absence_Seven_One.as_view(), name='delete_absence_seven_one'),
    path('admin_dashboard_absence_seven_two/<int:pk>/', views.Delete_Absence_Seven_Two.as_view(), name='delete_absence_seven_two'),
    path('admin_dashboard_absence_eight_one/<int:pk>/', views.Delete_Absence_Eight_One.as_view(), name='delete_absence_eight_one'),
    path('admin_dashboard_absence_eight_two/<int:pk>/', views.Delete_Absence_Eight_Two.as_view(), name='delete_absence_eight_two'),
    path('admin_dashboard_absence_nine_one/<int:pk>/', views.Delete_Absence_Nine_One.as_view(), name='delete_absence_nine_one'),
    path('admin_dashboard_absence_nine_two/<int:pk>/', views.Delete_Absence_Nine_Two.as_view(), name='delete_absence_nine_two'),

    # ====================================================================

    # Admin Dashboard Staff:
    path('admin_dashboard_staff/', views.Admin_Panel_Staff.as_view(), name='admin_dashboard_staff'),

    # Add Staff
    path('admin_dashboard_staff_add/', views.Add_Staff.as_view(), name='Add Staff'),

    # Delete Admin Dashboard Staff
    path('delete_staff/<int:pk>/', views.Delete_Staff.as_view(), name='Delete Staff'),


    # ====================================================================

    # Admin Dashboard News:
    path('admin_dashboard_news/', views.Admin_Panel_News.as_view(), name='admin_dashboard_news'),

    # Add News
    path('admin_dashboard_news_add/', views.Add_News.as_view(), name='Add News'),

    # Delete Admin Dashboard News
    path('delete_news/<int:pk>/', views.Delete_News.as_view(), name='Delete News'),

    # ====================================================================

    # ====================================================================

    # Admin Dashboard Facilities
    path('admin_dashboard_facilities/', views.Admin_Panel_Facilities.as_view(), name='admin_dashboard_facilities'),

    # Add Facilities
    path('admin_dashboard_facilities_add/', views.Add_Facilities.as_view(), name='Add Facilities'),

    # Delete Admin Dashboard Facilities
    path('delete_facilities/<int:pk>/', views.Delete_Facilities.as_view(), name='Delete Facilities'),

    # ====================================================================

    # ====================================================================

    # Admin Dashboard Contact
    path('admin_dashboard_contact/', views.Admin_Panel_Contact.as_view(), name='admin_dashboard_contact'),

    # Delete Admin Dashboard Contact
    path('delete_contact/<int:pk>/', views.Delete_Contact.as_view(), name='Delete Contact'),

    # ====================================================================

    # ====================================================================

    # Admin Dashboard Service
    path('admin_dashboard_service/', views.Admin_Panel_Service.as_view(), name='admin_dashboard_service'),

    # Add Service
    path('admin_dashboard_service_add/', views.Add_Service.as_view(), name='Add Service'),

    # Delete Admin Dashboard Service
    path('delete_service/<int:pk>/', views.Delete_Service.as_view(), name='Delete Service'),

    # ====================================================================

# ====================================================================

    # Admin Dashboard Common
    path('admin_dashboard_common/', views.Admin_Panel_Common.as_view(), name='admin_dashboard_common'),

    # Delete Admin Dashboard Service
    path('delete_common/<int:pk>/', views.Delete_Comman.as_view(), name='Delete Common'),

    # ====================================================================
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
