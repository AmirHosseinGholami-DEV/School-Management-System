from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.Student_Score_Mehr.as_view(), name="student"),
    path("score_aban/", views.Student_Score_Aban.as_view(), name="Aban Score"),
    path("score_azar/", views.Student_Score_Azar.as_view(), name="Azar Score"),
    path("score_dey/", views.Student_Score_Dey.as_view(), name="Dey Score"),
    path("score_bahman/", views.Student_Score_Bahman.as_view(), name="Bahman Score"),
    path("score_esfand/", views.Student_Score_Esfand.as_view(), name="Esfand Score"),
    path("score_farvardin/", views.Student_Score_Farvardin.as_view(), name="Farvardin Score"),
    path("score_ordibehesht/", views.Student_Score_Ordibeheshet.as_view(), name="Ordibehesht Score"),
    path("score_khordad/", views.Student_Score_Khordad.as_view(), name="Khordad Score"),
    # ... other url patterns

    path("change/", views.ChangeUP.as_view(), name="Change Page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
