from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.StudentRegisterView.as_view(), name='signup'),
    path('login1/', views.LoginView.as_view(), name='login'),
    path('teacher/', include("Teacher.urls"), name='teacher'),
    path("student/", include("Student.urls"), name="student"),
    path("management/", include("management.urls"), name="management"),
    path('admin/', include("Admin.urls"), name='admin'),
]