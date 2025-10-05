from django.views.generic import TemplateView
from Teacher.models import (
    Seven_Teacher_One, Seven_Teacher_Two, Eight_Teacher_One, 
    Eight_Teacher_Two, Nine_Teacher_One, Nine_Teacher_Two
)


# Teacher List View

class Teacher_Seven_One_List(TemplateView):
    template_name = 'Teacher List/Seven One.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher_seven_one'] = Seven_Teacher_One.objects.all()
        return context


class Teacher_Seven_Two_List(TemplateView):
    template_name = 'Teacher List/Seven Two.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher_seven_two'] = Seven_Teacher_Two.objects.all()
        return context


class Teacher_Eight_One_List(TemplateView):
    template_name = 'Teacher List/Eight One.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher_eight_one'] = Eight_Teacher_One.objects.all()
        return context


class Teacher_Eight_Two_List(TemplateView):
    template_name = 'Teacher List/Eight Two.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher_eight_two'] = Eight_Teacher_Two.objects.all()
        return context


class Teacher_Nine_One_List(TemplateView):
    template_name = 'Teacher List/Nine One.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher_nine_one'] = Nine_Teacher_One.objects.all()
        return context


class Teacher_Nine_Two_List(TemplateView):
    template_name = 'Teacher List/Nine Two.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher_nine_two'] = Nine_Teacher_Two.objects.all()
        return context
