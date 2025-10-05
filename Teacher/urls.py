from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.UserPanel_Mehr_View.as_view(), name="teacher"),
    path("aban/", views.UserPanel_Aban_View.as_view(), name="teacher_Aban"),
    path("azar/", views.UserPanel_Azar_View.as_view(), name="teacher_Azar"),
    path("absence/", views.UserPanelAbsenceView.as_view(), name="teacher_absence"),
    path('delete-absence/<int:student_id>/<str:selected_class>/', views.DeleteStudentAbsenceView.as_view(), name='delete_absence'),
    path("change/", views.ChangeUP.as_view(), name="Change Page Teacher"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
