from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from absence.models import (
    Seven_One_Absence, Seven_Two_Absence, Eight_One_Absence,
    Eight_Two_Absence, Nine_One_Absence, Nine_Two_Absence
)
from Teacher.models import (
    Seven_Teacher_One, Seven_Teacher_Two,
    Eight_Teacher_One, Eight_Teacher_Two,
    Nine_Teacher_One, Nine_Teacher_Two
)
from Student.models import (
    Seven_Student_One, Seven_Student_Two,
    Eight_Student_One, Eight_Student_Two,
    Nine_Student_One, Nine_Student_Two
)
from Staff.models import Staff
import logging

# Set up logging for debugging and error tracking
logger = logging.getLogger(__name__)


# Decorator to require user login for all views in this module
@method_decorator(login_required, name='dispatch')
class BaseStudentView(TemplateView):
    """
    Base class for handling student views.
    """

    def get_context_data(self, **kwargs):
        """
        Custom context to include staff details and student data.
        """
        context = super().get_context_data(**kwargs)
        username = self.request.user.username

        # Check if the logged-in user is a staff member
        try:
            staff = Staff.objects.get(username=username)
        except Staff.DoesNotExist:
            logger.warning(f"Staff with username '{username}' does not exist.")
            return render(self.request, 'error.html', {'message': 'Teacher information not available'})

        context['staff'] = staff
        context['students'] = self.get_students()
        return context

    def get_students(self):
        """
        Should be overridden in child classes to return specific student data.
        """
        return []


# Student views inheriting from BaseStudentView
class Seven_One_Student(BaseStudentView):
    template_name = "Management Page/Students/Seven One/Admin.html"

    def get_students(self):
        return Seven_Student_One.objects.all()


class Seven_Two_Student(BaseStudentView):
    template_name = "Management Page/Students/Seven Two/Admin.html"

    def get_students(self):
        return Seven_Student_Two.objects.all()


class Eight_One_Student(BaseStudentView):
    template_name = "Management Page/Students/Eight One/Admin.html"

    def get_students(self):
        return Eight_Student_One.objects.all()


class Eight_Two_Student(BaseStudentView):
    template_name = "Management Page/Students/Eight Two/Admin.html"

    def get_students(self):
        return Eight_Student_Two.objects.all()


class Nine_One_Student(BaseStudentView):
    template_name = "Management Page/Students/Nine One/Admin.html"

    def get_students(self):
        return Nine_Student_One.objects.all()


class Nine_Two_Student(BaseStudentView):
    template_name = "Management Page/Students/Nine Two/Admin.html"

    def get_students(self):
        return Nine_Student_Two.objects.all()


@method_decorator(login_required, name='dispatch')
class BaseTeacherView(TemplateView):
    """
    Base class for handling teacher views.
    """

    def get_context_data(self, **kwargs):
        """
        Custom context to include staff details and teacher data.
        """
        context = super().get_context_data(**kwargs)
        username = self.request.user.username

        # Check if the logged-in user is a staff member
        try:
            staff = Staff.objects.get(username=username)
        except Staff.DoesNotExist:
            logger.warning(f"Staff with username '{username}' does not exist.")
            return render(self.request, 'error.html', {'message': 'Teacher information not available'})

        context['staff'] = staff
        context['teachers'] = self.get_teachers()
        return context

    def get_teachers(self):
        """
        Should be overridden in child classes to return specific teacher data.
        """
        return []


# Teacher views inheriting from BaseTeacherView
class Seven_One_Teacher(BaseTeacherView):
    template_name = "Management Page/Teachers/Seven One/Admin.html"

    def get_teachers(self):
        return Seven_Teacher_One.objects.all()


class Seven_Two_Teacher(BaseTeacherView):
    template_name = "Management Page/Teachers/Seven Two/Admin.html"

    def get_teachers(self):
        return Seven_Teacher_Two.objects.all()


class Eight_One_Teacher(BaseTeacherView):
    template_name = "Management Page/Teachers/Eight One/Admin.html"

    def get_teachers(self):
        return Eight_Teacher_One.objects.all()


class Eight_Two_Teacher(BaseTeacherView):
    template_name = "Management Page/Teachers/Eight Two/Admin.html"

    def get_teachers(self):
        return Eight_Teacher_Two.objects.all()


class Nine_One_Teacher(BaseTeacherView):
    template_name = "Management Page/Teachers/Nine One/Admin.html"

    def get_teachers(self):
        return Nine_Teacher_One.objects.all()


class Nine_Two_Teacher(BaseTeacherView):
    template_name = "Management Page/Teachers/Nine Two/Admin.html"

    def get_teachers(self):
        return Nine_Teacher_Two.objects.all()


# ================= Staff Panel =============================

@method_decorator(login_required, name='dispatch')
class StaffList(TemplateView):
    """
    View for displaying the staff list.
    """
    template_name = "Management Page/Staff/Admin.html"

    def get_context_data(self, **kwargs):
        """
        Custom context to include staff details.
        """
        context = super().get_context_data(**kwargs)
        username = self.request.user.username

        try:
            staff = Staff.objects.get(username=username)
        except Staff.DoesNotExist:
            logger.warning(f"Staff with username '{username}' does not exist.")
            return render(self.request, 'error.html', {'message': 'Staff information not available'})

        context['staff'] = staff
        context["Staff_List"] = Staff.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class BaseAbsenceView(TemplateView):
    """
    Base class for handling teacher views.
    """

    def get_context_data(self, **kwargs):
        """
        Custom context to include staff details and teacher data.
        """
        context = super().get_context_data(**kwargs)
        username = self.request.user.username

        # Check if the logged-in user is a staff member
        try:
            staff = Staff.objects.get(username=username)
        except Staff.DoesNotExist:
            logger.warning(f"Staff with username '{username}' does not exist.")
            return render(self.request, 'error.html', {'message': 'Teacher information not available'})

        context['staff'] = staff
        context['absence'] = self.get_absence()
        return context

    def get_absence(self):
        """
        Should be overridden in child classes to return specific teacher data.
        """
        return []


# Teacher views inheriting from BaseTeacherView
class Seven_One_Absence(BaseTeacherView):
    template_name = "Management Page/Absence/Seven One/Admin.html"

    def get_absence(self):
        return Seven_One_Absence.objects.all()


class Seven_Two_Absence(BaseTeacherView):
    template_name = "Management Page/Absence/Seven Two/Admin.html"

    def get_absence(self):
        return Seven_Two_Absence.objects.all()


class Eight_One_Absence(BaseTeacherView):
    template_name = "Management Page/Absence/Eight One/Admin.html"

    def get_absence(self):
        return Eight_One_Absence.objects.all()


class Eight_Two_Absence(BaseTeacherView):
    template_name = "Management Page/Absence/Eight Two/Admin.html"

    def get_absence(self):
        return Eight_Two_Absence.objects.all()


class Nine_One_Absence(BaseTeacherView):
    template_name = "Management Page/Absence/Nine One/Admin.html"

    def get_absence(self):
        return Nine_One_Absence.objects.all()


class Nine_Two_Absence(BaseTeacherView):
    template_name = "Management Page/Absence/Nine Two/Admin.html"

    def get_absence(self):
        return Nine_Two_Absence.objects.all()