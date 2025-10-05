# ================= Imports Start =============================

# Django Core Libraries
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

# Models
from Admin.models import Admin_Web
from Facilities.models import Facilities
from Service.models import Service
from Staff.models import Staff
from Contact.models import Contact
from News.models import News
from Student.models import (
    Seven_Student_One, Seven_Student_Two, 
    Eight_Student_One, Eight_Student_Two, 
    Nine_Student_One, Nine_Student_Two
)
from absence.models import (
    Seven_One_Absence, Seven_Two_Absence, Eight_One_Absence,
    Eight_Two_Absence, Nine_One_Absence, Nine_Two_Absence
)
from Teacher.models import (
    Seven_Teacher_One, Seven_Teacher_Two, 
    Eight_Teacher_One, Eight_Teacher_Two, 
    Nine_Teacher_One, Nine_Teacher_Two
)
from common.models import Common

# Forms
from .forms import (
    Seven_Student_One_Form, Seven_Student_Two_Form, 
    Eight_Student_One_Form, Eight_Student_Two_Form, 
    Nine_Student_One_Form, Nine_Student_Two_Form, 
    Seven_Teacher_One_Form, Seven_Teacher_Two_Form, 
    Eight_Teacher_One_Form, Eight_Teacher_Two_Form, 
    Nine_Teacher_One_Form, Nine_Teacher_Two_Form,
    News_Form, Facilities_Form, Staff_Form, Service_Form
)

# Helpers
from .mixins import AdminRequiredMixin
from django.core.files.storage import FileSystemStorage

# ================= Imports End =============================

# ===================== Student Panel Views Start ====================

# Admin Panel Views for Class 7 Section 1
class Admin_Panel_Seven_One(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Students/Seven One/Admin.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data for the admin panel of class 7, section 1.
        """
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['students_seven_one'] = Seven_Student_One.objects.order_by('class_number')
        return context

# View to delete a student from Class 7, Section 1
class Delete_Student_Seven_One(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        """
        Delete a student from Class 7, Section 1.
        """
        student_id = kwargs.get('pk')
        student = Seven_Student_One.objects.get(id=student_id)
        student.delete()
        return redirect(reverse('admin_dashboard'))
    
# View to update a student from Class 7, Section 1
class Update_Student_Seven_One(LoginRequiredMixin, AdminRequiredMixin, View):
    """
        Update a student from Class 7, Section 1.
    """
    def post(self, request, pk):
        student = get_object_or_404(Seven_Student_One, id=pk)
        student.name = request.POST.get('name')
        student.class_number = request.POST.get('class_number')
        student.father_name = request.POST.get('father_name')
        student.username = request.POST.get('username')
        student.password = request.POST.get('password')
        student.father_Phone = request.POST.get('father_Phone')
        student.Mother_Phone = request.POST.get('Mother_Phone')
        if 'photo' in request.FILES:
            student.photo = request.FILES['photo']
        student.save()
        return redirect('admin_dashboard')


# Admin Panel Views for Class 7 Section 2
class Admin_Panel_Seven_Two(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Students/Seven Two/Admin.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data for the admin panel of class 7, section 2.
        """
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['students_seven_two'] = Seven_Student_Two.objects.order_by('class_number')
        return context

# View to delete a student from Class 7, Section 2
class Delete_Student_Seven_Two(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        """
        Delete a student from Class 7, Section 2.
        """
        student_id = kwargs.get('pk')
        student = Seven_Student_Two.objects.get(id=student_id)
        student.delete()
        return redirect(reverse('admin_dashboard_seven_two'))
    
# View to update a student from Class 7, Section 2
class Update_Student_Seven_Two(LoginRequiredMixin, AdminRequiredMixin, View):
    """
        Update a student from Class 7, Section 2.
    """
    def post(self, request, pk):
        student = get_object_or_404(Seven_Student_Two, id=pk)
        student.name = request.POST.get('name')
        student.class_number = request.POST.get('class_number')
        student.father_name = request.POST.get('father_name')
        student.username = request.POST.get('username')
        student.password = request.POST.get('password')
        student.father_Phone = request.POST.get('father_Phone')
        student.Mother_Phone = request.POST.get('Mother_Phone')
        if 'photo' in request.FILES:
            student.photo = request.FILES['photo']
        student.save()
        return redirect('admin_dashboard_seven_two')

# Admin Panel Views for Class 8 Section 1
class Admin_Panel_Eight_One(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Students/Eight One/Admin.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data for the admin panel of class 8, section 1.
        """
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['students_eight_one'] = Eight_Student_One.objects.order_by('class_number')
        return context

# View to delete a student from Class 8, Section 1
class Delete_Student_Eight_One(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        """
        Delete a student from Class 8, Section 1.
        """
        student_id = kwargs.get('pk')
        student = Eight_Student_One.objects.get(id=student_id)
        student.delete()
        return redirect(reverse('admin_dashboard_eight_one'))
    
# View to update a student from Class 8, Section 1
class Update_Student_Eight_One(LoginRequiredMixin, AdminRequiredMixin, View):
    """
        Update a student from Class 8, Section 1.
    """
    def post(self, request, pk):
        student = get_object_or_404(Eight_Student_One, id=pk)
        student.name = request.POST.get('name')
        student.class_number = request.POST.get('class_number')
        student.father_name = request.POST.get('father_name')
        student.username = request.POST.get('username')
        student.password = request.POST.get('password')
        student.father_Phone = request.POST.get('father_Phone')
        student.Mother_Phone = request.POST.get('Mother_Phone')
        if 'photo' in request.FILES:
            student.photo = request.FILES['photo']
        student.save()
        return redirect('admin_dashboard_eight_one')

# Admin Panel Views for Class 8 Section 2
class Admin_Panel_Eight_Two(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Students/Eight Two/Admin.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data for the admin panel of class 8, section 2.
        """
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['students_eight_two'] = Eight_Student_Two.objects.order_by('class_number')
        return context

# View to delete a student from Class 8, Section 2
class Delete_Student_Eight_Two(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        """
        Delete a student from Class 8, Section 2.
        """
        student_id = kwargs.get('pk')
        student = Eight_Student_Two.objects.get(id=student_id)
        student.delete()
        return redirect(reverse('admin_dashboard_eight_two'))
    
# View to update a student from Class 8, Section 2
class Update_Student_Eight_Two(LoginRequiredMixin, AdminRequiredMixin, View):
    """
        Update a student from Class 8, Section 2.
    """
    def post(self, request, pk):
        student = get_object_or_404(Eight_Student_Two, id=pk)
        student.name = request.POST.get('name')
        student.class_number = request.POST.get('class_number')
        student.father_name = request.POST.get('father_name')
        student.username = request.POST.get('username')
        student.password = request.POST.get('password')
        student.father_Phone = request.POST.get('father_Phone')
        student.Mother_Phone = request.POST.get('Mother_Phone')
        if 'photo' in request.FILES:
            student.photo = request.FILES['photo']
        student.save()
        return redirect('admin_dashboard_eight_two')


# Admin Panel Views for Class 9 Section 1
class Admin_Panel_Nine_One(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Students/Nine One/Admin.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data for the admin panel of class 9, section 1.
        """
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['students_nine_one'] = Nine_Student_One.objects.order_by('class_number')
        return context

# View to delete a student from Class 9, Section 1
class Delete_Student_Nine_One(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        """
        Delete a student from Class 9, Section 1.
        """
        student_id = kwargs.get('pk')
        student = Nine_Student_One.objects.get(id=student_id)
        student.delete()
        return redirect(reverse('admin_dashboard_nine_one'))

# View to update a student from Class 9, Section 1
class Update_Student_Nine_One(LoginRequiredMixin, AdminRequiredMixin, View):
    """
        Update a student from Class 9, Section 1.
    """
    def post(self, request, pk):
        student = get_object_or_404(Nine_Student_One, id=pk)
        student.name = request.POST.get('name')
        student.class_number = request.POST.get('class_number')
        student.father_name = request.POST.get('father_name')
        student.username = request.POST.get('username')
        student.password = request.POST.get('password')
        student.father_Phone = request.POST.get('father_Phone')
        student.Mother_Phone = request.POST.get('Mother_Phone')
        if 'photo' in request.FILES:
            student.photo = request.FILES['photo']
        student.save()
        return redirect('admin_dashboard_nine_one')
    
# Admin Panel Views for Class 9 Section 2
class Admin_Panel_Nine_Two(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Students/Nine Two/Admin.html'

    def get_context_data(self, **kwargs):
        """
        Get the context data for the admin panel of class 9, section 2.
        """
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['students_nine_two'] = Nine_Student_Two.objects.order_by('class_number')
        return context

# View to delete a student from Class 9, Section 2
class Delete_Student_Nine_Two(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        """
        Delete a student from Class 9, Section 2.
        """
        student_id = kwargs.get('pk')
        student = Nine_Student_Two.objects.get(id=student_id)
        student.delete()
        return redirect(reverse('admin_dashboard_nine_two'))
    
# View to update a student from Class 9, Section 2
class Update_Student_Nine_Two(LoginRequiredMixin, AdminRequiredMixin, View):
    """
        Update a student from Class 9, Section 2.
    """
    def post(self, request, pk):
        student = get_object_or_404(Nine_Student_Two, id=pk)
        student.name = request.POST.get('name')
        student.class_number = request.POST.get('class_number')
        student.father_name = request.POST.get('father_name')
        student.username = request.POST.get('username')
        student.password = request.POST.get('password')
        student.father_Phone = request.POST.get('father_Phone')
        student.Mother_Phone = request.POST.get('Mother_Phone')
        if 'photo' in request.FILES:
            student.photo = request.FILES['photo']
        student.save()
        return redirect('admin_dashboard_nine_two')

# ===================== Add Student Views ===========================

# View for adding a student (generic Add Student Page)
class Add_Student(TemplateView):
    template_name = "Admin Page/Students/Add Student/Add.html"

    def get_context_data(self, **kwargs):
        """
        Add the admin users to the context for the Add Student page.
        """
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        return context


# Adding student to Class 7, Section 1
class Add_Student_Seven_One(LoginRequiredMixin, TemplateView):
    template_name = 'Admin Page/Students/Add Student/Add.html'

    def get_context_data(self, **kwargs):
        """
        Add the form for adding a student to class 7, section 1 to the context.
        """
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['form_student_seven_one'] = kwargs.get('form_student_seven_one', Seven_Student_One_Form())
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle the form submission for adding a student to class 7, section 1.
        """
        form_student_seven_one = Seven_Student_One_Form(request.POST, request.FILES)

        if form_student_seven_one.is_valid():
            form_student_seven_one.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form_student_seven_one=form_student_seven_one))

    def get_success_url(self):
        """
        Redirect to the Add Student Seven One page after successful submission.
        """
        return reverse_lazy('Add Student Seven One')


# Adding student to Class 7, Section 2
class Add_Student_Seven_Two(LoginRequiredMixin, TemplateView):
    template_name = 'Admin Page/Students/Add Student/Add.html'

    def get_context_data(self, **kwargs):
        """
        Add the form for adding a student to class 7, section 2 to the context.
        """
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['form_student_seven_two'] = kwargs.get('form_student_seven_two', Seven_Student_Two_Form())
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle the form submission for adding a student to class 7, section 2.
        """
        form_student_seven_two = Seven_Student_Two_Form(request.POST, request.FILES)

        if form_student_seven_two.is_valid():
            form_student_seven_two.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form_student_seven_two=form_student_seven_two))

    def get_success_url(self):
        """
        Redirect to the Add Student Seven Two page after successful submission.
        """
        return reverse_lazy('Add Student Seven Two')

# The pattern continues for Classes 8 and 9 as well...



# Adding student to Class 8, Section 1
class Add_Student_Eight_One(LoginRequiredMixin, TemplateView):
    template_name = 'Admin Page/Students/Add Student/Add.html'

    def get_context_data(self, **kwargs):
        """
        Add the form for adding a student to class 8, section 1 to the context.
        """
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['form_student_eight_one'] = kwargs.get('form_student_eight_one', Eight_Student_One_Form())
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle the form submission for adding a student to class 8, section 1.
        """
        form_student_eight_one = Eight_Student_One_Form(request.POST, request.FILES)

        if form_student_eight_one.is_valid():
            form_student_eight_one.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form_student_eight_one=form_student_eight_one))

    def get_success_url(self):
        """
        Redirect to the Add Student Eight One page after successful submission.
        """
        return reverse_lazy('Add Student Eight One')


# Adding student to Class 8, Section 2
class Add_Student_Eight_Two(LoginRequiredMixin, TemplateView):
    template_name = 'Admin Page/Students/Add Student/Add.html'

    def get_context_data(self, **kwargs):
        """
        Add the form for adding a student to class 8, section 2 to the context.
        """
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['form_student_eight_two'] = kwargs.get('form_student_eight_two', Eight_Student_Two_Form())
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle the form submission for adding a student to class 8, section 2.
        """
        form_student_eight_two = Eight_Student_Two_Form(request.POST, request.FILES)

        if form_student_eight_two.is_valid():
            form_student_eight_two.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form_student_eight_two=form_student_eight_two))

    def get_success_url(self):
        """
        Redirect to the Add Student Eight Two page after successful submission.
        """
        return reverse_lazy('Add Student Eight Two')


# Adding student to Class 9, Section 1
class Add_Student_Nine_One(LoginRequiredMixin, TemplateView):
    template_name = 'Admin Page/Students/Add Student/Add.html'

    def get_context_data(self, **kwargs):
        """
        Add the form for adding a student to class 9, section 1 to the context.
        """
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['form_student_nine_one'] = kwargs.get('form_student_nine_one', Nine_Student_One_Form())
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle the form submission for adding a student to class 9, section 1.
        """
        form_student_nine_one = Nine_Student_One_Form(request.POST, request.FILES)

        if form_student_nine_one.is_valid():
            form_student_nine_one.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form_student_nine_one=form_student_nine_one))

    def get_success_url(self):
        """
        Redirect to the Add Student Nine One page after successful submission.
        """
        return reverse_lazy('Add Student Nine One')


# Adding student to Class 9, Section 2
class Add_Student_Nine_Two(LoginRequiredMixin, TemplateView):
    template_name = 'Admin Page/Students/Add Student/Add.html'

    def get_context_data(self, **kwargs):
        """
        Add the form for adding a student to class 9, section 2 to the context.
        """
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['form_student_nine_two'] = kwargs.get('form_student_nine_two', Nine_Student_Two_Form())
        return context

    def post(self, request, *args, **kwargs):
        """
        Handle the form submission for adding a student to class 9, section 2.
        """
        form_student_nine_two = Nine_Student_Two_Form(request.POST, request.FILES)

        if form_student_nine_two.is_valid():
            form_student_nine_two.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form_student_nine_two=form_student_nine_two))

    def get_success_url(self):
        """
        Redirect to the Add Student Nine Two page after successful submission.
        """
        return reverse_lazy('Add Student Nine Two')
        

# ================= Student Panel End =============================

# ================= Teacher Panel Start =============================

# This section handles the management of teachers in the Admin Panel.

# View for displaying the Admin Dashboard for teachers of class 7, section 1
class Admin_Panel_Teacher_Seven_One(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Teachers/Seven One/Admin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['teacher_seven_one'] = Seven_Teacher_One.objects.all()
        return context

# View for deleting a teacher from class 7, section 1
class Delete_Teacher_Seven_One(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        teacher_id = kwargs.get('pk')
        teacher = Seven_Teacher_One.objects.get(id=teacher_id)
        teacher.delete()
        return redirect(reverse('admin_dashboard_teacher_seven_one'))
    
# View to update a teacher from Class 7, Section 1
class Update_Teacher_Seven_One(LoginRequiredMixin, AdminRequiredMixin, View):
    """
        Update a teacher from Class 7, Section 1.
    """
    def post(self, request, pk):
        teacher = get_object_or_404(Seven_Teacher_One, id=pk)
        teacher.name = request.POST.get('name')
        teacher.password = request.POST.get('username')
        teacher.password = request.POST.get('password')
        teacher.course = request.POST.get('course')
        teacher.phone_number = request.POST.get('phone_number')
        if 'photo' in request.FILES:
            teacher.photo = request.FILES['photo']
        teacher.save()
        return redirect('admin_dashboard_teacher_seven_one')

# View for displaying the Admin Dashboard for teachers of class 7, section 2
class Admin_Panel_Teacher_Seven_Two(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Teachers/Seven Two/Admin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['teacher_seven_two'] = Seven_Teacher_Two.objects.all()
        return context

# View for deleting a teacher from class 7, section 2
class Delete_Teacher_Seven_Two(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        teacher_id = kwargs.get('pk')
        teacher = Seven_Teacher_Two.objects.get(id=teacher_id)
        teacher.delete()
        return redirect(reverse('admin_dashboard_teacher_seven_two'))
    
# View to update a teacher from Class 7, Section 2
class Update_Teacher_Seven_Two(LoginRequiredMixin, AdminRequiredMixin, View):
    """
        Update a teacher from Class 7, Section 2.
    """
    def post(self, request, pk):
        teacher = get_object_or_404(Seven_Teacher_Two, id=pk)
        teacher.name = request.POST.get('name')
        teacher.password = request.POST.get('username')
        teacher.password = request.POST.get('password')
        teacher.course = request.POST.get('course')
        teacher.phone_number = request.POST.get('phone_number')
        if 'photo' in request.FILES:
            teacher.photo = request.FILES['photo']
        teacher.save()
        return redirect('admin_dashboard_teacher_seven_two')

# View for displaying the Admin Dashboard for teachers of class 8, section 1
class Admin_Panel_Teacher_Eight_One(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Teachers/Eight One/Admin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['teacher_eight_one'] = Eight_Teacher_One.objects.all()
        return context

# View for deleting a teacher from class 8, section 1
class Delete_Teacher_Eight_One(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        teacher_id = kwargs.get('pk')
        teacher = Eight_Teacher_One.objects.get(id=teacher_id)
        teacher.delete()
        return redirect(reverse('admin_dashboard_teacher_eight_one'))
    
# View to update a teacher from Class 8, Section 1
class Update_Teacher_Eight_One(LoginRequiredMixin, AdminRequiredMixin, View):
    """
        Update a teacher from Class 8, Section 1.
    """
    def post(self, request, pk):
        teacher = get_object_or_404(Eight_Teacher_One, id=pk)
        teacher.name = request.POST.get('name')
        teacher.password = request.POST.get('username')
        teacher.password = request.POST.get('password')
        teacher.course = request.POST.get('course')
        teacher.phone_number = request.POST.get('phone_number')
        if 'photo' in request.FILES:
            teacher.photo = request.FILES['photo']
        teacher.save()
        return redirect('admin_dashboard_teacher_eight_one')

# View for displaying the Admin Dashboard for teachers of class 8, section 2
class Admin_Panel_Teacher_Eight_Two(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Teachers/Eight Two/Admin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['teacher_eight_two'] = Eight_Teacher_Two.objects.all()
        return context

# View for deleting a teacher from class 8, section 2
class Delete_Teacher_Eight_Two(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        teacher_id = kwargs.get('pk')
        teacher = Eight_Teacher_Two.objects.get(id=teacher_id)
        teacher.delete()
        return redirect(reverse('admin_dashboard_teacher_eight_two'))
    
# View to update a teacher from Class 7, Section 2
class Update_Teacher_Eight_Two(LoginRequiredMixin, AdminRequiredMixin, View):
    """
        Update a teacher from Class 8, Section 2.
    """
    def post(self, request, pk):
        teacher = get_object_or_404(Eight_Teacher_Two, id=pk)
        teacher.name = request.POST.get('name')
        teacher.password = request.POST.get('username')
        teacher.password = request.POST.get('password')
        teacher.course = request.POST.get('course')
        teacher.phone_number = request.POST.get('phone_number')
        if 'photo' in request.FILES:
            teacher.photo = request.FILES['photo']
        teacher.save()
        return redirect('admin_dashboard_teacher_eight_two')

# View for displaying the Admin Dashboard for teachers of class 9, section 1
class Admin_Panel_Teacher_Nine_One(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Teachers/Nine One/Admin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['teacher_nine_one'] = Nine_Teacher_One.objects.all()
        return context

# View for deleting a teacher from class 9, section 1
class Delete_Teacher_Nine_One(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        teacher_id = kwargs.get('pk')
        teacher = Nine_Teacher_One.objects.get(id=teacher_id)
        teacher.delete()
        return redirect(reverse('admin_dashboard_teacher_nine_one'))
    
# View to update a teacher from Class 9, Section 1
class Update_Teacher_Nine_One(LoginRequiredMixin, AdminRequiredMixin, View):
    """
        Update a teacher from Class 9, Section 1.
    """
    def post(self, request, pk):
        teacher = get_object_or_404(Nine_Teacher_One, id=pk)
        teacher.name = request.POST.get('name')
        teacher.password = request.POST.get('username')
        teacher.password = request.POST.get('password')
        teacher.course = request.POST.get('course')
        teacher.phone_number = request.POST.get('phone_number')
        if 'photo' in request.FILES:
            teacher.photo = request.FILES['photo']
        teacher.save()
        return redirect('admin_dashboard_teacher_nine_one')

# View for displaying the Admin Dashboard for teachers of class 9, section 2
class Admin_Panel_Teacher_Nine_Two(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Teachers/Nine Two/Admin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['teacher_nine_two'] = Nine_Teacher_Two.objects.all()
        return context

# View for deleting a teacher from class 9, section 2
class Delete_Teacher_Nine_Two(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        teacher_id = kwargs.get('pk')
        teacher = Nine_Teacher_Two.objects.get(id=teacher_id)
        teacher.delete()
        return redirect(reverse('admin_dashboard_teacher_nine_two'))
    
# View to update a teacher from Class 7, Section 2
class Update_Teacher_Nine_Two(LoginRequiredMixin, AdminRequiredMixin, View):
    """
        Update a teacher from Class 9, Section 2.
    """
    def post(self, request, pk):
        teacher = get_object_or_404(Nine_Teacher_Two, id=pk)
        teacher.name = request.POST.get('name')
        teacher.password = request.POST.get('username')
        teacher.password = request.POST.get('password')
        teacher.course = request.POST.get('course')
        teacher.phone_number = request.POST.get('phone_number')
        if 'photo' in request.FILES:
            teacher.photo = request.FILES['photo']
        teacher.save()
        return redirect('admin_dashboard_teacher_nine_two')

# ================= Add Teacher Views ============================

class Add_Teacher(TemplateView):
    template_name = "Admin Page/Teachers/Add Teacher/Add.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        return context

# Adding teacher to Class 7, Section 1
class Add_Teacher_Seven_One(LoginRequiredMixin, TemplateView):
    template_name = "Admin Page/Teachers/Add Teacher/Add.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['form_teacher_seven_one'] = kwargs.get('form_teacher_seven_one', Seven_Teacher_One_Form())
        return context

    def post(self, request, *args, **kwargs):
        form_teacher_seven_one = Seven_Teacher_One_Form(request.POST, request.FILES)

        if form_teacher_seven_one.is_valid():
            form_teacher_seven_one.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form_teacher_seven_one=form_teacher_seven_one))

    def get_success_url(self):
        return reverse_lazy('Add Teacher Seven One')

# Adding teacher to Class 7, Section 2
class Add_Teacher_Seven_Two(LoginRequiredMixin, TemplateView):
    template_name = "Admin Page/Teachers/Add Teacher/Add.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['form_teacher_seven_two'] = kwargs.get('form_teacher_seven_two', Seven_Teacher_Two_Form())
        return context

    def post(self, request, *args, **kwargs):
        form_teacher_seven_two = Seven_Teacher_Two_Form(request.POST, request.FILES)

        if form_teacher_seven_two.is_valid():
            form_teacher_seven_two.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form_teacher_seven_two=form_teacher_seven_two))

    def get_success_url(self):
        return reverse_lazy('Add Teacher Seven Two')

# Adding teacher to Class 8, Section 1
class Add_Teacher_Eight_One(LoginRequiredMixin, TemplateView):
    template_name = "Admin Page/Teachers/Add Teacher/Add.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['form_teacher_eight_one'] = kwargs.get('form_teacher_eight_one', Eight_Teacher_One_Form())
        return context

    def post(self, request, *args, **kwargs):
        form_teacher_eight_one = Eight_Teacher_One_Form(request.POST, request.FILES)

        if form_teacher_eight_one.is_valid():
            form_teacher_eight_one.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form_teacher_eight_one=form_teacher_eight_one))

    def get_success_url(self):
        return reverse_lazy('Add Teacher Eight One')

# Adding teacher to Class 8, Section 2
class Add_Teacher_Eight_Two(LoginRequiredMixin, TemplateView):
    template_name = "Admin Page/Teachers/Add Teacher/Add.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['form_teacher_eight_two'] = kwargs.get('form_teacher_eight_two', Eight_Teacher_Two_Form())
        return context

    def post(self, request, *args, **kwargs):
        form_teacher_eight_two = Eight_Teacher_Two_Form(request.POST, request.FILES)

        if form_teacher_eight_two.is_valid():
            form_teacher_eight_two.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form_teacher_eight_two=form_teacher_eight_two))

    def get_success_url(self):
        return reverse_lazy('Add Teacher Eight Two')

# Adding teacher to Class 9, Section 1
class Add_Teacher_Nine_One(LoginRequiredMixin, TemplateView):
    template_name = "Admin Page/Teachers/Add Teacher/Add.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['form_teacher_nine_one'] = kwargs.get('form_teacher_nine_one', Nine_Teacher_One_Form())
        return context

    def post(self, request, *args, **kwargs):
        form_teacher_nine_one = Nine_Teacher_One_Form(request.POST, request.FILES)

        if form_teacher_nine_one.is_valid():
            form_teacher_nine_one.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form_teacher_nine_one=form_teacher_nine_one))

    def get_success_url(self):
        return reverse_lazy('Add Teacher Nine One')

# Adding teacher to Class 9, Section 2
class Add_Teacher_Nine_Two(LoginRequiredMixin, TemplateView):
    template_name = "Admin Page/Teachers/Add Teacher/Add.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['form_teacher_nine_two'] = kwargs.get('form_teacher_nine_two', Nine_Teacher_Two_Form())
        return context

    def post(self, request, *args, **kwargs):
        form_teacher_nine_two = Nine_Teacher_Two_Form(request.POST, request.FILES)

        if form_teacher_nine_two.is_valid():
            form_teacher_nine_two.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form_teacher_nine_two=form_teacher_nine_two))

    def get_success_url(self):
        return reverse_lazy('Add Teacher Nine Two')

# ================= Teacher Panel End =============================

# ================= Staff Panel Start =============================

# This section handles the management of staff in the Admin Panel.

# View for displaying the Admin Dashboard for staff
class Admin_Panel_Staff(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Staff/List Staff/Admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['staff'] = Staff.objects.all()
        return context


# View for deleting a staff
class Delete_Staff(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        staff_id = kwargs.get('pk')
        staff = Staff.objects.get(id=staff_id)
        staff.delete()
        return redirect(reverse('admin_dashboard_staff'))


class Add_Staff(LoginRequiredMixin, TemplateView):
    template_name = "Admin Page/Staff/Add Staff/Add.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['form_staff'] = kwargs.get('form_staff', Staff_Form())
        return context

    def post(self, request, *args, **kwargs):
        form_staff = Staff_Form(request.POST, request.FILES)

        if form_staff.is_valid():
            form_staff.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form_staff=form_staff))

        return self.render_to_response(self.get_context_data(form_staff=form_staff))

    def get_success_url(self):
        return reverse_lazy('admin_dashboard_staff')

# ================= Staff Panel End =============================

# ================= Absence Panel Start =============================

# This section handles the management of absence in the Admin Panel.

# View for displaying the Admin Dashboard for absence of class 7, section 1
class Admin_Panel_Absence_Seven_One(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Absence/Seven One/Admin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['absence_seven_one'] = Seven_One_Absence.objects.all()
        return context

# View for deleting a absence from class 7, section 1
class Delete_Absence_Seven_One(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        student_id = kwargs.get('pk')
        student = Seven_One_Absence.objects.get(id=student_id)
        student.delete()
        return redirect(reverse('admin_dashboard_absence_seven_one'))


# View for displaying the Admin Dashboard for absence of class 7, section 2
class Admin_Panel_Absence_Seven_Two(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Absence/Seven Two/Admin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['absence_seven_two'] = Seven_Two_Absence.objects.all()
        return context

# View for deleting a absence from class 7, section 2
class Delete_Absence_Seven_Two(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        student_id = kwargs.get('pk')
        student = Seven_Two_Absence.objects.get(id=student_id)
        student.delete()
        return redirect(reverse('admin_dashboard_absence_seven_two'))


# View for displaying the Admin Dashboard for absence of class 8, section 1
class Admin_Panel_Absence_Eight_One(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Absence/Eight One/Admin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['absence_eight_one'] = Eight_One_Absence.objects.all()
        return context

# View for deleting a absence from class 8, section 1
class Delete_Absence_Eight_One(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        student_id = kwargs.get('pk')
        student = Eight_One_Absence.objects.get(id=student_id)
        student.delete()
        return redirect(reverse('admin_dashboard_absence_eight_one'))


# View for displaying the Admin Dashboard for absence of class 8, section 2
class Admin_Panel_Absence_Eight_Two(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Absence/Eight Two/Admin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['absence_eight_two'] = Eight_Two_Absence.objects.all()
        return context

# View for deleting a absence from class 8, section 2
class Delete_Absence_Eight_Two(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        student_id = kwargs.get('pk')
        student = Eight_Two_Absence.objects.get(id=student_id)
        student.delete()
        return redirect(reverse('admin_dashboard_absence_eight_two'))


# View for displaying the Admin Dashboard for absence of class 9, section 1
class Admin_Panel_Absence_Nine_One(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Absence/Nine One/Admin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['absence_nine_one'] = Nine_One_Absence.objects.all()
        return context

# View for deleting a absence from class 9, section 1
class Delete_Absence_Nine_One(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        student_id = kwargs.get('pk')
        student = Nine_One_Absence.objects.get(id=student_id)
        student.delete()
        return redirect(reverse('admin_dashboard_absence_nine_one'))


# View for displaying the Admin Dashboard for absence of class 9, section 2
class Admin_Panel_Absence_Nine_Two(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Absence/Nine Two/Admin.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['absence_nine_two'] = Nine_Two_Absence.objects.all()
        return context

# View for deleting a absence from class 9, section 2
class Delete_Absence_Nine_Two(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        student_id = kwargs.get('pk')
        student = Nine_Two_Absence.objects.get(id=student_id)
        student.delete()
        return redirect(reverse('admin_dashboard_absence_nine_two'))

# ================= Absence Panel End =============================

# ================= News Panel Start =============================

# This section handles the management of News in the Admin Panel.

# View for displaying the Admin Dashboard for news
class Admin_Panel_News(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/News/List/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['news'] = News.objects.all()
        return context

# View for adding news
class Add_News(LoginRequiredMixin, TemplateView):
    template_name = 'Admin Page/News/Add/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['news_form'] = kwargs.get('news_form', News_Form())
        return context

    def post(self, request, *args, **kwargs):
        news_form = News_Form(request.POST, request.FILES)

        if news_form.is_valid():
            # Save the news without checking for duplicate author
            news_form.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(news_form=news_form))

    def get_success_url(self):
        return reverse_lazy('admin_dashboard_news')


# View for deleting a news
class Delete_News(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        news_id = kwargs.get('pk')
        news = News.objects.get(id=news_id)
        news.delete()
        return redirect(reverse('admin_dashboard_news'))

# ================= News Panel End =============================

# ================= Facilities Panel Start =============================

# This section handles the management of Facilities in the Admin Panel.

# View for displaying the Admin Dashboard for Facilities
class Admin_Panel_Facilities(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Facilities/List Facilities/Admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['facilities'] = Facilities.objects.all()
        return context


# View for adding facilities
class Add_Facilities(LoginRequiredMixin, TemplateView):
    template_name = 'Admin Page/Facilities/Add Facilities/Add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['facilities_form'] = kwargs.get('facilities_form', Facilities_Form())
        return context

    def post(self, request, *args, **kwargs):
        facilities_form = Facilities_Form(request.POST, request.FILES)

        if facilities_form.is_valid():
            facilities_form.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(facilities_form=facilities_form))

        return self.render_to_response(self.get_context_data(facilities_form=facilities_form))

    def get_success_url(self):
        return reverse_lazy('admin_dashboard_facilities')


# View for deleting a Facility
class Delete_Facilities(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        facilities_id = kwargs.get('pk')
        facilities = Facilities.objects.get(id=facilities_id)
        facilities.delete()
        return redirect(reverse('admin_dashboard_facilities'))

# ================= Facilities Panel End =============================

# ================= Contact Panel Start =============================

# This section handles the management of Contact in the Admin Panel.

# View for displaying the Admin Dashboard for Contact
class Admin_Panel_Contact(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Contact/Admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['contact'] = Contact.objects.all()
        return context


# View for deleting a Contact
class Delete_Contact(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        contact_id = kwargs.get('pk')
        contact = Contact.objects.get(id=contact_id)
        contact.delete()
        return redirect(reverse('admin_dashboard_contact'))

# ================= Contact Panel End =============================

# ================= Service Panel Start =============================

# This section handles the management of Service in the Admin Panel.

# View for displaying the Admin Dashboard for Service
class Admin_Panel_Service(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Service/List Service/Admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['service'] = Service.objects.all()
        return context


class Add_Service(LoginRequiredMixin, TemplateView):
    template_name = 'Admin Page/Service/Add Service/Add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['service_form'] = kwargs.get('service_form', Service_Form())
        return context

    def post(self, request, *args, **kwargs):
        service_form = Service_Form(request.POST, request.FILES)

        if service_form.is_valid():
            service_form.save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(service_form=service_form))

        return self.render_to_response(self.get_context_data(service_form=service_form))

    def get_success_url(self):
        return reverse_lazy('admin_dashboard_service')


# View for deleting a Service
class Delete_Service(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        service_id = kwargs.get('pk')
        service = Service.objects.get(id=service_id)
        service.delete()
        return redirect(reverse('admin_dashboard_service'))

# ================= Service Panel End =============================

# ================= Common Panel Start =============================

# This section handles the management of Common in the Admin Panel.

# View for displaying the Admin Dashboard for Common
class Admin_Panel_Common(LoginRequiredMixin, AdminRequiredMixin, TemplateView):
    template_name = 'Admin Page/Common/Admin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Admin_Web.objects.all()
        context['common'] = Common.objects.all()
        return context


# View for deleting a Common
class Delete_Comman(LoginRequiredMixin, AdminRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        common_id = kwargs.get('pk')
        common = Common.objects.get(id=common_id)
        common.delete()
        return redirect(reverse('admin_dashboard_common'))

# ================= Common Panel End =============================