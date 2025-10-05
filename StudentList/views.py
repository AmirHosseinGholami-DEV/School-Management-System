from django.views.generic import TemplateView
from Student.models import (
    Seven_Student_One, Seven_Student_Two, Eight_Student_One,
    Eight_Student_Two, Nine_Student_One, Nine_Student_Two
)

# Dictionary to map models to their respective templates
STUDENT_LIST_VIEWS = {
    'seven_one': (Seven_Student_One, 'Student List/Seven One.html'),
    'seven_two': (Seven_Student_Two, 'Student List/Seven Two.html'),
    'eight_one': (Eight_Student_One, 'Student List/Eight One.html'),
    'eight_two': (Eight_Student_Two, 'Student List/Eight Two.html'),
    'nine_one': (Nine_Student_One, 'Student List/Nine One.html'),
    'nine_two': (Nine_Student_Two, 'Student List/Nine Two.html'),
}

class BaseStudentListView(TemplateView):
    """
    Generic base view for student lists.
    The child classes will define which student group they want to display.
    """
    model = None
    template_name = None
    context_key = None

    def get_context_data(self, **kwargs):
        """
        Add student data to the context.
        """
        context = super().get_context_data(**kwargs)
        if self.model:
            context[self.context_key] = self.model.objects.all()
        return context

# Dynamically creating classes for each student group

class Student_Seven_One_List(BaseStudentListView):
    model, template_name = STUDENT_LIST_VIEWS['seven_one']
    context_key = 'student_seven_one'

class Student_Seven_Two_List(BaseStudentListView):
    model, template_name = STUDENT_LIST_VIEWS['seven_two']
    context_key = 'student_seven_two'

class Student_Eight_One_List(BaseStudentListView):
    model, template_name = STUDENT_LIST_VIEWS['eight_one']
    context_key = 'student_eight_one'

class Student_Eight_Two_List(BaseStudentListView):
    model, template_name = STUDENT_LIST_VIEWS['eight_two']
    context_key = 'student_eight_two'

class Student_Nine_One_List(BaseStudentListView):
    model, template_name = STUDENT_LIST_VIEWS['nine_one']
    context_key = 'student_nine_one'

class Student_Nine_Two_List(BaseStudentListView):
    model, template_name = STUDENT_LIST_VIEWS['nine_two']
    context_key = 'student_nine_two'
