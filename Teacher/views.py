from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
import logging
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views import View
from SevenOneBook.models import (
    Fizik as Seven_One_Fizik, Shimi as Seven_One_Shimi,
    Zist as Seven_One_Zist, Math as Seven_One_Math,
    Farsi as Seven_One_Farsi, Emla as Seven_One_Emla,
    Negaresh as Seven_One_Negaresh, English as Seven_One_English,
    Arabic as Seven_One_Arabic, Quran as Seven_One_Quran,
    Maref as Seven_One_Maref, Kar_Fan as Seven_One_Kar_Fan,
    Computer as Seven_One_Computer, Motaleat as Seven_One_Motaleat,
    Tafakor as Seven_One_Tafakor, Farhang_Honar as Seven_One_Farhang_Honar, 
    Varzesh as Seven_One_Varzesh
)
from SevenTwoBook.models import (
    Fizik as Seven_Two_Fizik, Shimi as Seven_Two_Shimi,
    Zist as Seven_Two_Zist, Math as Seven_Two_Math,
    Farsi as Seven_Two_Farsi, Emla as Seven_Two_Emla,
    Negaresh as Seven_Two_Negaresh, English as Seven_Two_English,
    Arabic as Seven_Two_Arabic, Quran as Seven_Two_Quran,
    Maref as Seven_Two_Maref, Kar_Fan as Seven_Two_Kar_Fan,
    Computer as Seven_Two_Computer, Motaleat as Seven_Two_Motaleat,
    Tafakor as Seven_Two_Tafakor, Farhang_Honar as Seven_Two_Farhang_Honar, 
    Varzesh as Seven_Two_Varzesh
)
from EightOneBook.models import (
    Fizik as Eight_One_Fizik, Shimi as Eight_One_Shimi,
    Zist as Eight_One_Zist, Math as Eight_One_Math,
    Farsi as Eight_One_Farsi, Emla as Eight_One_Emla,
    Negaresh as Eight_One_Negaresh, English as Eight_One_English,
    Arabic as Eight_One_Arabic, Quran as Eight_One_Quran,
    Maref as Eight_One_Maref, Kar_Fan as Eight_One_Kar_Fan,
    Computer as Eight_One_Computer, Motaleat as Eight_One_Motaleat,
    Tafakor as Eight_One_Tafakor, Farhang_Honar as Eight_One_Farhang_Honar, 
    Varzesh as Eight_One_Varzesh
)
from EightTwoBook.models import (
    Fizik as Eight_Two_Fizik, Shimi as Eight_Two_Shimi,
    Zist as Eight_Two_Zist, Math as Eight_Two_Math,
    Farsi as Eight_Two_Farsi, Emla as Eight_Two_Emla,
    Negaresh as Eight_Two_Negaresh, English as Eight_Two_English,
    Arabic as Eight_Two_Arabic, Quran as Eight_Two_Quran,
    Maref as Eight_Two_Maref, Kar_Fan as Eight_Two_Kar_Fan,
    Computer as Eight_Two_Computer, Motaleat as Eight_Two_Motaleat,
    Tafakor as Eight_Two_Tafakor, Farhang_Honar as Eight_Two_Farhang_Honar, 
    Varzesh as Eight_Two_Varzesh
)
from NineOneBook.models import (
    Fizik as Nine_One_Fizik, Shimi as Nine_One_Shimi,
    Zist as Nine_One_Zist, Math as Nine_One_Math,
    Farsi as Nine_One_Farsi, Emla as Nine_One_Emla,
    Negaresh as Nine_One_Negaresh, English as Nine_One_English,
    Arabic as Nine_One_Arabic, Quran as Nine_One_Quran,
    Maref as Nine_One_Maref, Kar_Fan as Nine_One_Kar_Fan,
    Computer as Nine_One_Computer, Motaleat as Nine_One_Motaleat,
    Amadegi as Nine_One_Amadegi, Farhang_Honar as Nine_One_Farhang_Honar, 
    Varzesh as Nine_One_Varzesh
)
from NineTwoBook.models import (
    Fizik as Nine_Two_Fizik, Shimi as Nine_Two_Shimi,
    Zist as Nine_Two_Zist, Math as Nine_Two_Math,
    Farsi as Nine_Two_Farsi, Emla as Nine_Two_Emla,
    Negaresh as Nine_Two_Negaresh, English as Nine_Two_English,
    Arabic as Nine_Two_Arabic, Quran as Nine_Two_Quran,
    Maref as Nine_Two_Maref, Kar_Fan as Nine_Two_Kar_Fan,
    Computer as Nine_Two_Computer, Motaleat as Nine_Two_Motaleat,
    Amadegi as Nine_Two_Amadegi, Farhang_Honar as Nine_Two_Farhang_Honar, 
    Varzesh as Nine_Two_Varzesh
)

from .models import (
    Seven_Teacher_One, Seven_Teacher_Two, Eight_Teacher_One, 
    Eight_Teacher_Two, Nine_Teacher_One, Nine_Teacher_Two
)
from Student.models import (
    Seven_Student_One, Seven_Student_Two, Eight_Student_One,
    Eight_Student_Two, Nine_Student_One, Nine_Student_Two
)
from absence.models import (
    Seven_One_Absence, Seven_Two_Absence, Eight_One_Absence,
    Eight_Two_Absence, Nine_One_Absence, Nine_Two_Absence
)





class_dict = {
        'هفتم یک': {
            'فیزیک': Seven_One_Fizik,
            'شیمی': Seven_One_Shimi,
            'زیست': Seven_One_Zist,
            'ریاضی': Seven_One_Math,
            'ادبیات': Seven_One_Farsi,
            'املا': Seven_One_Emla,
            'نگارش': Seven_One_Negaresh,
            'انگلیسی': Seven_One_English,
            'عربی': Seven_One_Arabic,
            'قرآن': Seven_One_Quran,
            'معارف': Seven_One_Maref,
            'کار و فن': Seven_One_Kar_Fan,
            'رایانه': Seven_One_Computer,
            'مطالعات': Seven_One_Motaleat,
            'تفکر': Seven_One_Tafakor,
            'فرهنگ و هنر': Seven_One_Farhang_Honar,
            'ورزش': Seven_One_Varzesh,
        },
        'هفتم دو': {
            'فیزیک': Seven_Two_Fizik,
            'شیمی': Seven_Two_Shimi,
            'زیست': Seven_Two_Zist,
            'ریاضی': Seven_Two_Math,
            'ادبیات': Seven_Two_Farsi,
            'املا': Seven_Two_Emla,
            'نگارش': Seven_Two_Negaresh,
            'انگلیسی': Seven_Two_English,
            'عربی': Seven_Two_Arabic,
            'قرآن': Seven_Two_Quran,
            'معارف': Seven_Two_Maref,
            'کار و فن': Seven_Two_Kar_Fan,
            'رایانه': Seven_Two_Computer,
            'مطالعات': Seven_Two_Motaleat,
            'تفکر': Seven_Two_Tafakor,
            'فرهنگ و هنر': Seven_Two_Farhang_Honar,
            'ورزش': Seven_Two_Varzesh,
        },
        'هشتم یک': {
            'فیزیک': Eight_One_Fizik,
            'شیمی': Eight_One_Shimi,
            'زیست': Eight_One_Zist,
            'ریاضی': Eight_One_Math,
            'ادبیات': Eight_One_Farsi,
            'املا': Eight_One_Emla,
            'نگارش': Eight_One_Negaresh,
            'انگلیسی': Eight_One_English,
            'عربی': Eight_One_Arabic,
            'قرآن': Eight_One_Quran,
            'معارف': Eight_One_Maref,
            'کار و فن': Eight_One_Kar_Fan,
            'رایانه': Eight_One_Computer,
            'مطالعات': Eight_One_Motaleat,
            'تفکر': Eight_One_Tafakor,
            'فرهنگ و هنر': Eight_One_Farhang_Honar,
            'ورزش': Eight_One_Varzesh,
        },
        'هشتم دو': {
            'فیزیک': Eight_Two_Fizik,
            'شیمی': Eight_Two_Shimi,
            'زیست': Eight_Two_Zist,
            'ریاضی': Eight_Two_Math,
            'ادبیات': Eight_Two_Farsi,
            'املا': Eight_Two_Emla,
            'نگارش': Eight_Two_Negaresh,
            'انگلیسی': Eight_Two_English,
            'عربی': Eight_Two_Arabic,
            'قرآن': Eight_Two_Quran,
            'معارف': Eight_Two_Maref,
            'کار و فن': Eight_Two_Kar_Fan,
            'رایانه': Eight_Two_Computer,
            'مطالعات': Eight_Two_Motaleat,
            'تفکر': Eight_Two_Tafakor,
            'فرهنگ و هنر': Eight_Two_Farhang_Honar,
            'ورزش': Eight_Two_Varzesh,
        },
        'نهم یک': {
            'فیزیک': Nine_One_Fizik,
            'شیمی': Nine_One_Shimi,
            'زیست': Nine_One_Zist,
            'ریاضی': Nine_One_Math,
            'ادبیات': Nine_One_Farsi,
            'املا': Nine_One_Emla,
            'نگارش': Nine_One_Negaresh,
            'انگلیسی': Nine_One_English,
            'عربی': Nine_One_Arabic,
            'قرآن': Nine_One_Quran,
            'معارف': Nine_One_Maref,
            'کار و فن': Nine_One_Kar_Fan,
            'رایانه': Nine_One_Computer,
            'مطالعات': Nine_One_Motaleat,
            'آمادگی': Nine_One_Amadegi,
            'فرهنگ و هنر': Nine_One_Farhang_Honar,
            'ورزش': Nine_One_Varzesh,
        },
        'نهم دو': {
            'فیزیک': Nine_Two_Fizik,
            'شیمی': Nine_Two_Shimi,
            'زیست': Nine_Two_Zist,
            'ریاضی': Nine_Two_Math,
            'ادبیات': Nine_Two_Farsi,
            'املا': Nine_Two_Emla,
            'نگارش': Nine_Two_Negaresh,
            'انگلیسی': Nine_Two_English,
            'عربی': Nine_Two_Arabic,
            'قرآن': Nine_Two_Quran,
            'معارف': Nine_Two_Maref,
            'کار و فن': Nine_Two_Kar_Fan,
            'رایانه': Nine_Two_Computer,
            'مطالعات': Nine_Two_Motaleat,
            'آمادگی': Nine_Two_Amadegi,
            'فرهنگ و هنر': Nine_Two_Farhang_Honar,
            'ورزش': Nine_Two_Varzesh,
        },
    }



        
# Logging configuration
logger = logging.getLogger(__name__)
@method_decorator(login_required, name='dispatch')
class UserPanel_Mehr_View(TemplateView):
    template_name = 'Teacher Page/Score_Mehr.html'

    def get_context_data(self, **kwargs):
        """
        This method is responsible for preparing the context data that will be passed to the template.
        It retrieves teacher information, student scores, and related data based on the logged-in user.
        """
        context = super().get_context_data(**kwargs)
        username = self.request.user.username  # Get the current logged-in teacher's username

        # Dictionary mapping teacher models to class names
        tables = {
            Seven_Teacher_One: 'هفتم یک',
            Seven_Teacher_Two: 'هفتم دو',
            Eight_Teacher_One: 'هشتم یک',
            Eight_Teacher_Two: 'هشتم دو',
            Nine_Teacher_One: 'نهم یک',
            Nine_Teacher_Two: 'نهم دو'
        }

        teachers = []  # List to store all teachers associated with the logged-in user
        teacher_classes = []  # List of classes taught by the teacher
        student_scores = {}  # Dictionary to store student scores for the selected month

        # Iterate through all teacher models to find the logged-in teacher
        for table, class_name in tables.items():
            try:
                teacher = table.objects.get(username=username)  # Fetch the teacher object
                teacher.teacher_class = class_name  # Assign the class name to the teacher object
                teachers.append(teacher)  # Add the teacher to the list
                teacher_classes.append(class_name)  # Add the class name to the list

                # Map student models to class names
                student_table_map = {
                    'هفتم یک': Seven_Student_One,
                    'هفتم دو': Seven_Student_Two,
                    'هشتم یک': Eight_Student_One,
                    'هشتم دو': Eight_Student_Two,
                    'نهم یک': Nine_Student_One,
                    'نهم دو': Nine_Student_Two,
                }

                # Get the corresponding student model for the teacher's class
                student_table = student_table_map.get(class_name)

                # Get the subject table based on the teacher's course and class
                subject_table = class_dict.get(class_name, {}).get(teacher.course)

                if subject_table:
                    # Fetch scores for students in the selected class and month
                    scores = subject_table.objects.filter(
                        name__in=[student.name for student in student_table.objects.all()],
                        month='مهر'
                    )
                    for score in scores:
                        student_scores[score.name] = score.score  # Store student scores in the dictionary

            except table.DoesNotExist:
                continue  # If the teacher is not found in this table, skip to the next one

        # If no teacher is found, return an error page
        if not teachers:
            return render(self.request, 'error.html', {'message': 'Teacher information not available'})

        # Get the selected class from the URL query parameters
        selected_class = self.request.GET.get('class', None)

        # Fetch students for the selected class
        students = []
        if selected_class:
            class_table_map = {
                'هفتم یک': Seven_Student_One,
                'هفتم دو': Seven_Student_Two,
                'هشتم یک': Eight_Student_One,
                'هشتم دو': Eight_Student_Two,
                'نهم یک': Nine_Student_One,
                'نهم دو': Nine_Student_Two,
            }
            student_table = class_table_map.get(selected_class)
            if student_table:
                students = student_table.objects.order_by('class_number')

        # Add all collected data to the context
        context['teachers'] = teachers
        context['teacher_classes'] = teacher_classes
        context['students'] = students
        context['selected_class'] = selected_class
        context['student_scores'] = student_scores

        return context
    

    def post(self, request, *args, **kwargs):
        """
        This method handles POST requests to update student scores for the selected class and month.
        It processes the submitted form data and updates the database accordingly.
        """
        username = request.user.username  # Get the current logged-in teacher's username

        # Map class names to their respective student models
        class_table_map = {
            'هفتم یک': Seven_Student_One,
            'هفتم دو': Seven_Student_Two,
            'هشتم یک': Eight_Student_One,
            'هشتم دو': Eight_Student_Two,
            'نهم یک': Nine_Student_One,
            'نهم دو': Nine_Student_Two,
        }

        # Get the selected class from the POST data
        selected_class = request.POST.get('class')

        # Validate the selected class
        if not selected_class or selected_class not in class_table_map:
            return JsonResponse({'error': 'Invalid selected class.'}, status=400)

        # Find the teacher in all teacher models
        teacher_models = [
            Seven_Teacher_One, Seven_Teacher_Two,
            Eight_Teacher_One, Eight_Teacher_Two,
            Nine_Teacher_One, Nine_Teacher_Two,
        ]

        teacher = None
        for model in teacher_models:
            try:
                teacher = model.objects.get(username=username)
                break
            except model.DoesNotExist:
                continue

        if not teacher:
            return JsonResponse({'error': 'Teacher information not found.'}, status=404)

        # Get the teacher's course and validate it
        teacher_course = teacher.course
        if teacher_course not in class_dict[selected_class]:
            return JsonResponse({'error': 'Invalid course for the selected class.'}, status=400)

        # Get the subject table for the selected class and course
        subject_table = class_dict[selected_class].get(teacher_course)
        if not subject_table:
            return JsonResponse({'error': 'Subject table not found.'}, status=400)

        # Process each score submitted in the POST data
        for key, value in request.POST.items():
            if key.startswith('score_'):  # Check if the key represents a student score
                try:
                    student_id = int(key.split('_')[1])  # Extract the student ID from the key
                    student = get_object_or_404(class_table_map[selected_class], id=student_id)  # Get the student object

                    # Set the score value to '0' if it is empty
                    score_value = value.strip() if value.strip() != '' else '0'

                    # Check if a record already exists for the student and month
                    existing_record = subject_table.objects.filter(
                        name=student.name,
                        month='مهر'
                    ).first()

                    if existing_record:
                        # Update the existing record with the new score
                        existing_record.score = score_value
                        existing_record.save()
                    else:
                        # Create a new record if none exists
                        subject_table.objects.create(
                            name=student.name,
                            month='مهر',
                            score=score_value
                        )

                except ValueError:
                    continue  # Skip invalid keys

        # Redirect back to the teacher dashboard after processing the scores
        return redirect("teacher")



# Logging configuration
logger = logging.getLogger(__name__)
@method_decorator(login_required, name='dispatch')
class UserPanel_Aban_View(TemplateView):
    template_name = 'Teacher Page/Score_Aban.html'

    def get_context_data(self, **kwargs):
        """
        This method prepares the context data to be passed to the template.
        It retrieves teacher information, student scores, and related data based on the logged-in user.
        """
        context = super().get_context_data(**kwargs)
        username = self.request.user.username  # Get the current logged-in teacher's username

        # Dictionary mapping teacher models to class names
        tables = {
            Seven_Teacher_One: 'هفتم یک',
            Seven_Teacher_Two: 'هفتم دو',
            Eight_Teacher_One: 'هشتم یک',
            Eight_Teacher_Two: 'هشتم دو',
            Nine_Teacher_One: 'نهم یک',
            Nine_Teacher_Two: 'نهم دو'
        }

        teachers = []  # List to store all teachers associated with the logged-in user
        teacher_classes = []  # List of classes taught by the teacher
        student_scores = {}  # Dictionary to store student scores for the selected month

        # Iterate through all teacher models to find the logged-in teacher
        for table, class_name in tables.items():
            try:
                teacher = table.objects.get(username=username)  # Fetch the teacher object
                teacher.teacher_class = class_name  # Assign the class name to the teacher object
                teachers.append(teacher)  # Add the teacher to the list
                teacher_classes.append(class_name)  # Add the class name to the list

                # Map student models to class names
                student_table_map = {
                    'هفتم یک': Seven_Student_One,
                    'هفتم دو': Seven_Student_Two,
                    'هشتم یک': Eight_Student_One,
                    'هشتم دو': Eight_Student_Two,
                    'نهم یک': Nine_Student_One,
                    'نهم دو': Nine_Student_Two,
                }

                # Get the corresponding student model for the teacher's class
                student_table = student_table_map.get(class_name)

                # Get the subject table based on the teacher's course and class
                subject_table = class_dict.get(class_name, {}).get(teacher.course)

                if subject_table:
                    # Fetch scores for students in the selected class and month
                    scores = subject_table.objects.filter(
                        name__in=[student.name for student in student_table.objects.all()],
                        month='آبان'
                    )
                    for score in scores:
                        student_scores[score.name] = score.score  # Store student scores in the dictionary

            except table.DoesNotExist:
                continue  # If the teacher is not found in this table, skip to the next one

        # If no teacher is found, return an error page
        if not teachers:
            return render(self.request, 'error.html', {'message': 'Teacher information not available'})

        # Get the selected class from the URL query parameters
        selected_class = self.request.GET.get('class', None)

        # Fetch students for the selected class
        students = []
        if selected_class:
            class_table_map = {
                'هفتم یک': Seven_Student_One,
                'هفتم دو': Seven_Student_Two,
                'هشتم یک': Eight_Student_One,
                'هشتم دو': Eight_Student_Two,
                'نهم یک': Nine_Student_One,
                'نهم دو': Nine_Student_Two,
            }
            student_table = class_table_map.get(selected_class)
            if student_table:
                students = student_table.objects.order_by('class_number')

        # Add all collected data to the context
        context['teachers'] = teachers
        context['teacher_classes'] = teacher_classes
        context['students'] = students
        context['selected_class'] = selected_class
        context['student_scores'] = student_scores

        return context

    def post(self, request, *args, **kwargs):
        """
        This method handles POST requests to update student scores for the selected class and month.
        It processes the submitted form data and updates the database accordingly.
        """
        username = request.user.username  # Get the current logged-in teacher's username

        # Map class names to their respective student models
        class_table_map = {
            'هفتم یک': Seven_Student_One,
            'هفتم دو': Seven_Student_Two,
            'هشتم یک': Eight_Student_One,
            'هشتم دو': Eight_Student_Two,
            'نهم یک': Nine_Student_One,
            'نهم دو': Nine_Student_Two,
        }

        # Get the selected class from the POST data
        selected_class = request.POST.get('class')

        # Validate the selected class
        if not selected_class or selected_class not in class_table_map:
            return JsonResponse({'error': 'Invalid selected class.'}, status=400)

        # Find the teacher in all teacher models
        teacher_models = [
            Seven_Teacher_One, Seven_Teacher_Two,
            Eight_Teacher_One, Eight_Teacher_Two,
            Nine_Teacher_One, Nine_Teacher_Two,
        ]

        teacher = None
        for model in teacher_models:
            try:
                teacher = model.objects.get(username=username)
                break
            except model.DoesNotExist:
                continue

        if not teacher:
            return JsonResponse({'error': 'Teacher information not found.'}, status=404)

        # Get the teacher's course and validate it
        teacher_course = teacher.course
        if teacher_course not in class_dict[selected_class]:
            return JsonResponse({'error': 'Invalid course for the selected class.'}, status=400)

        # Get the subject table for the selected class and course
        subject_table = class_dict[selected_class].get(teacher_course)
        if not subject_table:
            return JsonResponse({'error': 'Subject table not found.'}, status=400)

        # Process each score submitted in the POST data
        for key, value in request.POST.items():
            if key.startswith('score_'):  # Check if the key represents a student score
                try:
                    student_id = int(key.split('_')[1])  # Extract the student ID from the key
                    student = get_object_or_404(class_table_map[selected_class], id=student_id)  # Get the student object

                    # Set the score value to '0' if it is empty
                    score_value = value.strip() if value.strip() != '' else '0'

                    # Check if a record already exists for the student and month
                    existing_record = subject_table.objects.filter(
                        name=student.name,
                        month='آبان'
                    ).first()

                    if existing_record:
                        # Update the existing record with the new score
                        existing_record.score = score_value
                        existing_record.save()
                    else:
                        # Create a new record if none exists
                        subject_table.objects.create(
                            name=student.name,
                            month='آبان',
                            score=score_value
                        )

                except ValueError:
                    continue  # Skip invalid keys

        # Redirect back to the teacher dashboard after processing the scores
        return redirect("teacher_Aban")






@method_decorator(login_required, name='dispatch')
class UserPanel_Azar_View(TemplateView):
    template_name = 'Teacher Page/Score_Azar.html'

    def get_context_data(self, **kwargs):
        """
        This method prepares the context data to be passed to the template.
        It retrieves teacher information, student scores, and related data based on the logged-in user.
        """
        context = super().get_context_data(**kwargs)
        username = self.request.user.username  # Get the current logged-in teacher's username

        # Dictionary mapping teacher models to class names
        tables = {
            Seven_Teacher_One: 'هفتم یک',
            Seven_Teacher_Two: 'هفتم دو',
            Eight_Teacher_One: 'هشتم یک',
            Eight_Teacher_Two: 'هشتم دو',
            Nine_Teacher_One: 'نهم یک',
            Nine_Teacher_Two: 'نهم دو'
        }

        teachers = []  # List to store all teachers associated with the logged-in user
        teacher_classes = []  # List of classes taught by the teacher
        student_scores = {}  # Dictionary to store student scores for the selected month

        # Iterate through all teacher models to find the logged-in teacher
        for table, class_name in tables.items():
            try:
                teacher = table.objects.get(username=username)  # Fetch the teacher object
                teacher.teacher_class = class_name  # Assign the class name to the teacher object
                teachers.append(teacher)  # Add the teacher to the list
                teacher_classes.append(class_name)  # Add the class name to the list

                # Map student models to class names
                student_table_map = {
                    'هفتم یک': Seven_Student_One,
                    'هفتم دو': Seven_Student_Two,
                    'هشتم یک': Eight_Student_One,
                    'هشتم دو': Eight_Student_Two,
                    'نهم یک': Nine_Student_One,
                    'نهم دو': Nine_Student_Two,
                }

                # Get the corresponding student model for the teacher's class
                student_table = student_table_map.get(class_name)

                # Get the subject table based on the teacher's course and class
                subject_table = class_dict.get(class_name, {}).get(teacher.course)

                if subject_table:
                    # Fetch scores for students in the selected class and month
                    scores = subject_table.objects.filter(
                        name__in=[student.name for student in student_table.objects.all()],
                        month='آذر'
                    )
                    for score in scores:
                        student_scores[score.name] = score.score  # Store student scores in the dictionary

            except table.DoesNotExist:
                continue  # If the teacher is not found in this table, skip to the next one

        # If no teacher is found, return an error page
        if not teachers:
            return render(self.request, 'error.html', {'message': 'Teacher information not available'})

        # Get the selected class from the URL query parameters
        selected_class = self.request.GET.get('class', None)

        # Fetch students for the selected class
        students = []
        if selected_class:
            class_table_map = {
                'هفتم یک': Seven_Student_One,
                'هفتم دو': Seven_Student_Two,
                'هشتم یک': Eight_Student_One,
                'هشتم دو': Eight_Student_Two,
                'نهم یک': Nine_Student_One,
                'نهم دو': Nine_Student_Two,
            }
            student_table = class_table_map.get(selected_class)
            if student_table:
                students = student_table.objects.order_by('class_number')

        # Add all collected data to the context
        context['teachers'] = teachers
        context['teacher_classes'] = teacher_classes
        context['students'] = students
        context['selected_class'] = selected_class
        context['student_scores'] = student_scores

        return context

    def post(self, request, *args, **kwargs):
        """
        This method handles POST requests to update student scores for the selected class and month.
        It processes the submitted form data and updates the database accordingly.
        """
        username = request.user.username  # Get the current logged-in teacher's username

        # Map class names to their respective student models
        class_table_map = {
            'هفتم یک': Seven_Student_One,
            'هفتم دو': Seven_Student_Two,
            'هشتم یک': Eight_Student_One,
            'هشتم دو': Eight_Student_Two,
            'نهم یک': Nine_Student_One,
            'نهم دو': Nine_Student_Two,
        }

        # Get the selected class from the POST data
        selected_class = request.POST.get('class')

        # Validate the selected class
        if not selected_class or selected_class not in class_table_map:
            return JsonResponse({'error': 'Invalid selected class.'}, status=400)

        # Find the teacher in all teacher models
        teacher_models = [
            Seven_Teacher_One, Seven_Teacher_Two,
            Eight_Teacher_One, Eight_Teacher_Two,
            Nine_Teacher_One, Nine_Teacher_Two,
        ]

        teacher = None
        for model in teacher_models:
            try:
                teacher = model.objects.get(username=username)
                break
            except model.DoesNotExist:
                continue

        if not teacher:
            return JsonResponse({'error': 'Teacher information not found.'}, status=404)

        # Get the teacher's course and validate it
        teacher_course = teacher.course
        if teacher_course not in class_dict[selected_class]:
            return JsonResponse({'error': 'Invalid course for the selected class.'}, status=400)

        # Get the subject table for the selected class and course
        subject_table = class_dict[selected_class].get(teacher_course)
        if not subject_table:
            return JsonResponse({'error': 'Subject table not found.'}, status=400)

        # Process each score submitted in the POST data
        for key, value in request.POST.items():
            if key.startswith('score_'):  # Check if the key represents a student score
                try:
                    student_id = int(key.split('_')[1])  # Extract the student ID from the key
                    student = get_object_or_404(class_table_map[selected_class], id=student_id)  # Get the student object

                    # Set the score value to '0' if it is empty
                    score_value = value.strip() if value.strip() != '' else '0'

                    # Check if a record already exists for the student and month
                    existing_record = subject_table.objects.filter(
                        name=student.name,
                        month='آذر'
                    ).first()

                    if existing_record:
                        # Update the existing record with the new score
                        existing_record.score = score_value
                        existing_record.save()
                    else:
                        # Create a new record if none exists
                        subject_table.objects.create(
                            name=student.name,
                            month='آذر',
                            score=score_value
                        )

                except ValueError:
                    continue  # Skip invalid keys

        # Redirect back to the teacher dashboard after processing the scores
        return redirect("teacher_Azar")
import jdatetime

@method_decorator(login_required, name='dispatch')
class UserPanelAbsenceView(TemplateView):
    template_name = 'Teacher Page/absence.html'

    def get_context_data(self, **kwargs):
        """
        This method prepares the context data to be passed to the template.
        It retrieves teacher information and related absence records based on the logged-in user.
        """
        context = super().get_context_data(**kwargs)
        username = self.request.user.username  # Get the current logged-in teacher's username

        # Log the requested username for debugging purposes
        logger.info(f"Requested username: {username}")

        # List of teacher models to search for the logged-in teacher
        teacher_models = [
            Seven_Teacher_One,
            Seven_Teacher_Two,
            Eight_Teacher_One,
            Eight_Teacher_Two,
            Nine_Teacher_One,
            Nine_Teacher_Two
        ]

        teachers = []  # List to store all teachers associated with the logged-in user

        # Search for the teacher in all teacher models
        for model in teacher_models:
            try:
                teacher = model.objects.get(username=username)
                teachers.append(teacher)  # Add the teacher to the list if found
            except model.DoesNotExist:
                continue  # Skip to the next model if the teacher is not found

        if not teachers:
            # If no teacher is found, return an error page
            return render(self.request, 'error.html', {'message': 'Teacher information not available'})

        # Set the first teacher as the active teacher
        context['teacher'] = teachers[0]

        # Map teacher models to class names
        class_map = {
            Seven_Teacher_One: 'هفتم یک',
            Seven_Teacher_Two: 'هفتم دو',
            Eight_Teacher_One: 'هشتم یک',
            Eight_Teacher_Two: 'هشتم دو',
            Nine_Teacher_One: 'نهم یک',
            Nine_Teacher_Two: 'نهم دو'
        }

        # Populate the list of classes taught by the teacher
        context['classes'] = [class_map[type(teacher)] for teacher in teachers]

        # Get the selected class from the POST or GET request
        selected_class = self.request.POST.get('class') or self.request.GET.get('class')

        if selected_class:
            # Map student models to class names
            student_models = {
                'هفتم یک': Seven_Student_One,
                'هفتم دو': Seven_Student_Two,
                'هشتم یک': Eight_Student_One,
                'هشتم دو': Eight_Student_Two,
                'نهم یک': Nine_Student_One,
                'نهم دو': Nine_Student_Two
            }

            # Fetch the corresponding student model for the selected class
            student_model = student_models.get(selected_class)

            if student_model:
                context['students'] = student_model.objects.order_by('class_number') # Get all students in the selected class

                # Map absence models to class names
                absence_models = {
                    'هفتم یک': Seven_One_Absence,
                    'هفتم دو': Seven_Two_Absence,
                    'هشتم یک': Eight_One_Absence,
                    'هشتم دو': Eight_Two_Absence,
                    'نهم یک': Nine_One_Absence,
                    'نهم دو': Nine_Two_Absence
                }

                # Fetch absence records for the selected class
                absence_model = absence_models.get(selected_class)
                if absence_model:
                    context['course_records'] = absence_model.objects.all()

        # Log the selected class for debugging purposes
        logger.debug(f"Selected class: {selected_class}")

        # Add the selected class to the context
        context['selected_class'] = selected_class

        return context

    def post(self, request, *args, **kwargs):
        """
        This method handles POST requests to create new absence records.
        It processes the submitted form data and saves the absence record to the database.
        """
        
        context = self.get_context_data(**kwargs)

        selected_class = request.POST.get('class')
        selected_student_name = request.POST.get('student')
        selected_day = request.POST.get('day')

        if selected_class and selected_student_name and selected_day:
            student_models = {
                'هفتم یک': Seven_Student_One,
                'هفتم دو': Seven_Student_Two,
                'هشتم یک': Eight_Student_One,
                'هشتم دو': Eight_Student_Two,
                'نهم یک': Nine_Student_One,
                'نهم دو': Nine_Student_Two
            }

            student_model = student_models.get(selected_class)
            student = student_model.objects.filter(name=selected_student_name).first() if student_model else None

            if student:
                teacher_models = [
                    Seven_Teacher_One, Seven_Teacher_Two,
                    Eight_Teacher_One, Eight_Teacher_Two,
                    Nine_Teacher_One, Nine_Teacher_Two
                ]

                teacher = None
                for model in teacher_models:
                    try:
                        teacher = model.objects.get(username=request.user.username)
                        break
                    except model.DoesNotExist:
                        continue

                if teacher:
                    absence_models = {
                        'هفتم یک': Seven_One_Absence,
                        'هفتم دو': Seven_Two_Absence,
                        'هشتم یک': Eight_One_Absence,
                        'هشتم دو': Eight_Two_Absence,
                        'نهم یک': Nine_One_Absence,
                        'نهم دو': Nine_Two_Absence
                    }

                    absence_model = absence_models.get(selected_class)

                    if absence_model:
                        shamsi_today = jdatetime.date.today().strftime('%Y/%m/%d')  # گرفتن تاریخ امروز شمسی
                        absence_model.objects.create(
                            name=student.name,
                            day=selected_day,
                            lessone=teacher.course,
                            shamsi_date=shamsi_today
                        )

        return render(request, self.template_name, context)


class DeleteStudentAbsenceView(LoginRequiredMixin, View):
    """
    This view handles the deletion of a student's absence record.
    It ensures that only authenticated users (teachers) can delete absence records.
    """

    def post(self, request, student_id, selected_class):
        """
        Handles POST requests to delete an absence record for a specific student and class.

        Parameters:
            - request: The HTTP request object.
            - student_id: The ID of the absence record to be deleted.
            - selected_class: The name of the class associated with the absence record.

        Returns:
            - Redirects the user back to the teacher's absence page after deletion.
        """

        # Fetch the logged-in teacher from all teacher models
        teacher_models = [
            Seven_Teacher_One,
            Seven_Teacher_Two,
            Eight_Teacher_One,
            Eight_Teacher_Two,
            Nine_Teacher_One,
            Nine_Teacher_Two,
        ]

        teacher = None
        for model in teacher_models:
            try:
                teacher = model.objects.get(username=request.user.username)
                break
            except model.DoesNotExist:
                continue

        if not teacher:
            # If the teacher is not found, redirect back to the absence page
            messages.error(request, "Teacher information not found.")
            return redirect('teacher_absence')

        # Map class names to their respective absence models
        absence_models = {
            'هفتم یک': Seven_One_Absence,
            'هفتم دو': Seven_Two_Absence,
            'هشتم یک': Eight_One_Absence,
            'هشتم دو': Eight_Two_Absence,
            'نهم یک': Nine_One_Absence,
            'نهم دو': Nine_Two_Absence,
        }

        # Validate the selected class
        if selected_class not in absence_models:
            messages.error(request, "Invalid selected class.")
            return redirect('teacher_absence')

        # Get the corresponding absence model for the selected class
        absence_model = absence_models[selected_class]

        try:
            # Fetch the absence record to be deleted
            record = get_object_or_404(absence_model, id=student_id)

            # Ensure the teacher has permission to delete this record
            if record.lessone != teacher.course:
                messages.error(request, "You do not have permission to delete this record.")
                return redirect('teacher_absence')

            # Delete the absence record
            record.delete()
            messages.success(request, "The absence record has been successfully deleted.")

        except absence_model.DoesNotExist:
            # If the record does not exist, show an error message and redirect
            messages.error(request, "The specified absence record does not exist.")

        # Redirect back to the teacher's absence page
        return redirect('teacher_absence')


class ChangeUP(LoginRequiredMixin, View):
    teacher_models = [
        Seven_Teacher_One, Seven_Teacher_Two, 
        Eight_Teacher_One, Eight_Teacher_Two,
        Nine_Teacher_One, Nine_Teacher_Two
    ]

    def get_teacher(self, user):
        """
        Search through all teacher models to find the user based on their username.
        Returns the teacher object if found, otherwise returns None.
        """
        for model in self.teacher_models:
            try:
                teacher = model.objects.get(username=user.username)
                return teacher  # Return the teacher if found
            except model.DoesNotExist:
                continue  # If not found, move to the next model
        return None  # Return None if the user is not found in any table

    def get(self, request):
        """
        Handle GET requests to display the teacher's current information on the change page.
        """
        teacher = self.get_teacher(request.user)

        if not teacher:
            # If the teacher is not found, show an error message or redirect to another appropriate page
            messages.error(request, "Teacher information not found.")
            return redirect('error_page')  # Replace 'error_page' with the actual error page URL name

        context = {
            'teacher': teacher
        }
        return render(request, 'Teacher Page/change.html', context)

    def post(self, request):
        """
        Handle POST requests to update the teacher's username, password, and profile photo.
        """
        teacher = self.get_teacher(request.user)

        if not teacher:
            # If the teacher is not found, show an error message or redirect to another appropriate page
            messages.error(request, "Teacher information not found.")
            return redirect('error_page')  # Replace 'error_page' with the actual error page URL name

        # Update Username
        new_username = request.POST.get('username')
        if new_username:
            # Check if the new username already exists
            if User.objects.filter(username=new_username).exists():
                messages.error(request, "The provided username already exists. Please choose a different one.")
                return redirect('Change Page Teacher')  # Redirect back to the change page

            # Update the username in the auth_user table
            user = User.objects.get(username=teacher.username)
            old_username = user.username  # Store the old username for updating other tables
            user.username = new_username
            user.save()

            # Update the username in all related teacher models
            for model in self.teacher_models:
                try:
                    related_teacher = model.objects.get(username=old_username)
                    related_teacher.username = new_username
                    related_teacher.save()
                except model.DoesNotExist:
                    continue

        # Update Password
        new_password = request.POST.get('password')
        if new_password:
            # Hash the new password and update it in the auth_user table
            user = User.objects.get(username=new_username if new_username else teacher.username)
            user.set_password(new_password)
            user.save()

            # Optionally, store the plain password in all related teacher models (if required)
            for model in self.teacher_models:
                try:
                    related_teacher = model.objects.get(username=new_username if new_username else teacher.username)
                    related_teacher.password = new_password  # Store the plain password if needed
                    related_teacher.save()
                except model.DoesNotExist:
                    continue

        # Update Profile Photo
        new_photo = request.FILES.get('photo')
        if new_photo:
            # Update the profile photo in all related teacher models
            for model in self.teacher_models:
                try:
                    related_teacher = model.objects.get(username=new_username if new_username else teacher.username)
                    related_teacher.photo = new_photo
                    related_teacher.save()
                except model.DoesNotExist:
                    continue

        # Success message and redirect
        messages.success(request, "Your information has been updated successfully.")
        return redirect('Change Page Teacher')  # Redirect to the change page or another appropriate page