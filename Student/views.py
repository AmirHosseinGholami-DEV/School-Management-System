from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from bidi.algorithm import get_display

# Importing models for different classes (Students and Books)
from Student.models import (
    Seven_Student_One, Seven_Student_Two, 
    Eight_Student_One, Eight_Student_Two, 
    Nine_Student_One, Nine_Student_Two
)

# Importing models from different book categories for each grade
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

# The code continues to implement the view or functionality...


# دیکشنری‌های دروس و نگاشت نام فارسی
SUBJECT_MAPPINGS = {
    'Seven_One': {
        Seven_One_Fizik: 'فیزیک', Seven_One_Shimi: 'شیمی', Seven_One_Zist: 'زیست', Seven_One_Math: 'ریاضی',
        Seven_One_Farsi: 'فارسی', Seven_One_Emla: 'املا', Seven_One_Negaresh: 'نگارش', Seven_One_English: 'انگلیسی',
        Seven_One_Arabic: 'عربی', Seven_One_Quran: 'قرآن', Seven_One_Maref: 'معارف', Seven_One_Kar_Fan: 'کار و فناوری',
        Seven_One_Computer: 'کامپیوتر', Seven_One_Motaleat: 'مطالعات', Seven_One_Tafakor: 'تفکر و پژوهش',
        Seven_One_Farhang_Honar: 'فرهنگ و هنر', Seven_One_Varzesh: 'ورزش'
    },

    'Seven_Two': {
        Seven_Two_Fizik: 'فیزیک', Seven_Two_Shimi: 'شیمی', Seven_Two_Zist: 'زیست', Seven_Two_Math: 'ریاضی',
        Seven_Two_Farsi: 'فارسی', Seven_Two_Emla: 'املا', Seven_Two_Negaresh: 'نگارش', Seven_Two_English: 'انگلیسی',
        Seven_Two_Arabic: 'عربی', Seven_Two_Quran: 'قرآن', Seven_Two_Maref: 'معارف', Seven_Two_Kar_Fan: 'کار و فناوری',
        Seven_Two_Computer: 'کامپیوتر', Seven_Two_Motaleat: 'مطالعات', Seven_Two_Tafakor: 'تفکر و پژوهش',
        Seven_Two_Farhang_Honar: 'فرهنگ و هنر', Seven_Two_Varzesh: 'ورزش'
    },

    'Eight_One': {
        Eight_One_Fizik: 'فیزیک', Eight_One_Shimi: 'شیمی', Eight_One_Zist: 'زیست', Eight_One_Math: 'ریاضی',
        Eight_One_Farsi: 'فارسی', Eight_One_Emla: 'املا', Eight_One_Negaresh: 'نگارش', Eight_One_English: 'انگلیسی',
        Eight_One_Arabic: 'عربی', Eight_One_Quran: 'قرآن', Eight_One_Maref: 'معارف', Eight_One_Kar_Fan: 'کار و فناوری',
        Eight_One_Computer: 'کامپیوتر', Eight_One_Motaleat: 'مطالعات', Eight_One_Tafakor: 'تفکر و پژوهش',
        Eight_One_Farhang_Honar: 'فرهنگ و هنر', Eight_One_Varzesh: 'ورزش'
    },

    'Eight_Two': {
        Eight_Two_Fizik: 'فیزیک', Eight_Two_Shimi: 'شیمی', Eight_Two_Zist: 'زیست', Eight_Two_Math: 'ریاضی',
        Eight_Two_Farsi: 'فارسی', Eight_Two_Emla: 'املا', Eight_Two_Negaresh: 'نگارش', Eight_Two_English: 'انگلیسی',
        Eight_Two_Arabic: 'عربی', Eight_Two_Quran: 'قرآن', Eight_Two_Maref: 'معارف', Eight_Two_Kar_Fan: 'کار و فناوری',
        Eight_Two_Computer: 'کامپیوتر', Eight_Two_Motaleat: 'مطالعات', Eight_Two_Tafakor: 'تفکر و پژوهش',
        Eight_Two_Farhang_Honar: 'فرهنگ و هنر', Eight_Two_Varzesh: 'ورزش'
    },

    'Nine_One': {
        Nine_One_Fizik: 'فیزیک', Nine_One_Shimi: 'شیمی', Nine_One_Zist: 'زیست', Nine_One_Math: 'ریاضی',
        Nine_One_Farsi: 'فارسی', Nine_One_Emla: 'املا', Nine_One_Negaresh: 'نگارش', Nine_One_English: 'انگلیسی',
        Nine_One_Arabic: 'عربی', Nine_One_Quran: 'قرآن', Nine_One_Maref: 'معارف', Nine_One_Kar_Fan: 'کار و فناوری',
        Nine_One_Computer: 'کامپیوتر', Nine_One_Motaleat: 'مطالعات', Nine_One_Amadegi: 'آمادگی دفاعی',
        Nine_One_Farhang_Honar: 'فرهنگ و هنر', Nine_One_Varzesh: 'ورزش'
    },

    'Nine_Two': {
        Nine_Two_Fizik: 'فیزیک', Nine_Two_Shimi: 'شیمی', Nine_Two_Zist: 'زیست', Nine_Two_Math: 'ریاضی',
        Nine_Two_Farsi: 'فارسی', Nine_Two_Emla: 'املا', Nine_Two_Negaresh: 'نگارش', Nine_Two_English: 'انگلیسی',
        Nine_Two_Arabic: 'عربی', Nine_Two_Quran: 'قرآن', Nine_Two_Maref: 'معارف', Nine_Two_Kar_Fan: 'کار و فناوری',
        Nine_Two_Computer: 'کامپیوتر', Nine_Two_Motaleat: 'مطالعات', Nine_Two_Amadegi: 'آمادگی دفاعی',
        Nine_Two_Farhang_Honar: 'فرهنگ و هنر', Nine_Two_Varzesh: 'ورزش'
    },
}

STUDENT_MODEL_MAPPINGS = {
    Seven_Student_One: SUBJECT_MAPPINGS['Seven_One'],
    Seven_Student_Two: SUBJECT_MAPPINGS['Seven_Two'],
    Eight_Student_One: SUBJECT_MAPPINGS['Eight_One'],
    Eight_Student_Two: SUBJECT_MAPPINGS['Eight_Two'],
    Nine_Student_One: SUBJECT_MAPPINGS['Nine_One'],
    Nine_Student_Two: SUBJECT_MAPPINGS['Nine_Two'],
}



class Student_Score_Mehr(View):

    def get_user_data(self, user):
        """
        Retrieves the student data based on the user's username.
        Returns the student data, subject models, and class name.
        """
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)

                # Identifying the student's class based on their model
                if isinstance(student_data, Seven_Student_One):
                    student_class = 'هفتم یک'
                elif isinstance(student_data, Seven_Student_Two):
                    student_class = 'هفتم دو'
                elif isinstance(student_data, Eight_Student_One):
                    student_class = 'هشتم یک'
                elif isinstance(student_data, Eight_Student_Two):
                    student_class = 'هشتم دو'
                elif isinstance(student_data, Nine_Student_One):
                    student_class = 'نهم یک'
                elif isinstance(student_data, Nine_Student_Two):
                    student_class = 'نهم دو'
                else:
                    student_class = 'نامشخص'

                return student_data, subjects, student_class

        return None, None, None  # Return None if no student found

    def get_subject_scores(self, student_name, subject_models):
        """
        Retrieves subject scores for the student and calculates the average scores for مهر and آبان.
        """
        subject_scores = []
        subject_scores_aban = []  # To store Aban scores
        total_score_mehr = 0
        total_score_aban = 0
        score_count_mehr = 0
        score_count_aban = 0

        # Loop through each subject model and get the scores for مهر and آبان
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='مهر')
            scores_aban = model.objects.filter(name=student_name, month='آبان')  # Aban scores

            # Add مهر scores
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,
                    'name': score.name,
                    'month': score.month,
                    'score': score.score,
                })
                total_score_mehr += float(score.score)
                score_count_mehr += 1

            # Add آبان scores
            for score in scores_aban:
                subject_scores_aban.append({
                    'subject': subject_name,
                    'name': score.name,
                    'month': score.month,
                    'score': score.score,
                })
                total_score_aban += float(score.score)
                score_count_aban += 1

        # Calculate average scores
        average_score_mehr = total_score_mehr / score_count_mehr if score_count_mehr > 0 else 0
        average_score_aban = total_score_aban / score_count_aban if score_count_aban > 0 else 0

        return subject_scores, average_score_mehr, subject_scores_aban, average_score_aban

    def generate_pdf(self, context):
        """
        Generates a PDF report for the student's scores.
        This includes student info, subject scores, and average scores.
        """
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="scores.pdf"'

        pdf_canvas = canvas.Canvas(response, pagesize=letter)
        width, height = letter

        # Register custom font for Persian text
        pdfmetrics.registerFont(TTFont('IRANSansWeb', 'static/Static Student/fonts/IRANSansWeb_Medium.ttf'))

        # Draw logos
        image1_path = 'static/Static Student/images/Logo.png'
        image2_path = 'static/Static Student/images/Iran_AmozeshoParvaresh.png'
        pdf_canvas.drawImage(image1_path, 5, height - 98, width=100, height=100, mask='auto')
        pdf_canvas.drawImage(image2_path, 520, height - 95, width=90, height=90, mask='auto')

        # Title
        title_text = "کارنامه هوشمند"
        title_text_reshaped = arabic_reshaper.reshape(title_text)
        title_text_bidi = get_display(title_text_reshaped)
        pdf_canvas.setFont("IRANSansWeb", 24)
        title_x = (width - pdf_canvas.stringWidth(title_text_bidi, "IRANSansWeb", 24)) / 2
        pdf_canvas.drawString(title_x, height - 25, title_text_bidi)

        # Student Info
        student_name_text = f"نام دانش آموز: {context['user_info']['name']}"
        student_id_text = f"نام کاربری: {context['user_info']['username']}"  # Assuming national ID is stored in username
        student_class_text = f"کلاس: {context['user_info']['student_class']}"
        year_text = "سال تحصیلی: 1404-1403"

        # Convert to bidirectional format
        student_name_text_bidi = get_display(arabic_reshaper.reshape(student_name_text))
        student_id_text_bidi = get_display(arabic_reshaper.reshape(student_id_text))
        student_class_text_bidi = get_display(arabic_reshaper.reshape(student_class_text))
        year_text_bidi = get_display(arabic_reshaper.reshape(year_text))

        # Set font and draw student info
        pdf_canvas.setFont("IRANSansWeb", 12)
        pdf_canvas.drawString(350, height - 60, student_name_text_bidi)
        pdf_canvas.drawString(190, height - 60, student_id_text_bidi)
        pdf_canvas.drawString(430, height - 90, student_class_text_bidi)
        pdf_canvas.drawString(145, height - 90, year_text_bidi)

        # Create the table header for subject scores
        headers = ['نمره آبان', 'نمره مهر', 'نام درس', 'ردیف']
        headers_reshaped = [get_display(arabic_reshaper.reshape(header)) for header in headers]
        data = [headers_reshaped]

        total_score = 0
        count_scores = len(context['user_info']['scores'])

        # Loop through scores and generate table rows
        for index, score in enumerate(context['user_info']['scores']):
            subject = score['subject']
            mehr_score = score['score']
            month_aban_score = next(
                (s['score'] for s in context['user_info']['scores_aban'] if s['subject'] == subject), None
            )

            data.append([
                str(month_aban_score) if month_aban_score else '-',  # Aban score
                str(mehr_score),  # Mehr score
                get_display(arabic_reshaper.reshape(subject)),  # Subject name
                str(index + 1),  # Row number
            ])
            total_score += float(score['score'])

        # Add averages to the table
        average_score_mehr = context['average_score']
        average_score_aban = context['average_score_aban']  # Aban average
        data.append([
            f"{average_score_aban:.2f}",
            f"{average_score_mehr:.2f}",
            get_display(arabic_reshaper.reshape("معدل")),
            str(count_scores + 1)
        ])

        # Adjust column widths and row heights
        col_widths = [100, 100, 130, 60]
        row_heights = [30] * (len(data) - 1) + [30]

        table = Table(data, colWidths=col_widths, rowHeights=row_heights)

        # Table style for better visualization
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'IRANSansWeb'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, len(data) - 1), (-1, len(data) - 1), colors.lightgrey),
            ('TEXTCOLOR', (0, len(data) - 1), (-1, len(data) - 1), colors.black),
            ('ALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'CENTER'),
            ('VALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'MIDDLE'),
        ]))

        # Position table in the center of the page
        table_width, table_height = table.wrap(0, 0)
        table_x = (width - table_width) / 2
        table_y = height - 180 - table_height

        # Draw the table on the Canvas
        table.drawOn(pdf_canvas, table_x, table_y)

        # Footer
        footer_height = 30
        footer_y = 0  # Footer at the bottom of the page
        footer_text = "سامانه هوشمند استعداد های درخشان زنده یاد کردی ساخته شده توسط امیر حسین غلامی"
        footer_text_reshaped = arabic_reshaper.reshape(footer_text)
        footer_text_bidi = get_display(footer_text_reshaped)

        # Draw footer background and text
        pdf_canvas.setFillColor(colors.lightgrey)
        pdf_canvas.rect(0, footer_y, width, footer_height, fill=True, stroke=False)
        pdf_canvas.setFont("IRANSansWeb", 12)
        footer_text_width = pdf_canvas.stringWidth(footer_text_bidi, "IRANSansWeb", 12)
        footer_text_x = (width - footer_text_width) / 2
        footer_text_y = footer_y + 8
        pdf_canvas.setFillColor(colors.black)
        pdf_canvas.drawString(footer_text_x, footer_text_y, footer_text_bidi)

        # Finalize PDF
        pdf_canvas.save()
        return response

    def get(self, request, *args, **kwargs):
        """
        Retrieves the student data and generates the score report in HTML or PDF format.
        """
        user = request.user
        student_data, subject_models, student_class = self.get_user_data(user)

        if student_data:
            subject_scores, average_score_mehr, subject_scores_aban, average_score_aban = self.get_subject_scores(
                student_data.name, subject_models)

            # Prepare context for rendering the score page
            context = {
                'user_info': {
                    'name': student_data.name,
                    'username': student_data.username,
                    'student_class': student_class,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores,
                    'scores_aban': subject_scores_aban,
                    'average_score': average_score_mehr
                },
                'average_score': average_score_mehr,
                'average_score_aban': average_score_aban,
            }

            # If the user wants to download the PDF
            if 'download_pdf' in request.GET:
                return self.generate_pdf(context)

            # Otherwise, render the scores in HTML
            return render(request, 'Student Page/Score/Mehr.html', context)
        else:
            # Handle case where the student is not found
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})


@method_decorator(login_required, name='dispatch')
class Student_Score_Aban(View):

    def get_user_data(self, user):
        """
        Retrieves the student data based on the user's username.
        Checks various student models to find matching data.
        """
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}  # Return None if no student found

    def get_subject_scores(self, student_name, subject_models):
        """
        Retrieves and calculates the scores for the student, 
        filtered by the 'آبان' month for each subject model.
        """
        subject_scores = []
        total_score = 0
        score_count = 0

        # Loop through each subject model and get the scores for "آبان"
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='آبان')
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # Persian subject name
                    'name': score.name,
                    'month': score.month,
                    'score': score.score,
                })
                total_score += float(score.score)
                score_count += 1

        average_score = total_score / score_count if score_count > 0 else 0
        return subject_scores, average_score

    def generate_pdf(self, context):
        """
        Generates a PDF report of the student's scores for "آبان".
        This includes images, title, subject scores, and footer.
        """
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="scores_aban.pdf"'

        # Create Canvas for PDF generation
        pdf_canvas = canvas.Canvas(response, pagesize=letter)
        width, height = letter  # Page size

        # Register Persian font
        pdfmetrics.registerFont(TTFont('IRANSansWeb', 'static/Static Student/fonts/IRANSansWeb_Medium.ttf'))

        # Add logos to the PDF
        image1_path = 'static/Static Student/images/Logo.png'
        image2_path = 'static/Static Student/images/Iran_AmozeshoParvaresh.png'
        pdf_canvas.drawImage(image1_path, 5, height - 98, width=100, height=100, mask='auto')
        pdf_canvas.drawImage(image2_path, 520, height - 95, width=90, height=90, mask='auto')

        # Title for the PDF
        title_text = "کارنامه آبان ماه"
        title_text_reshaped = arabic_reshaper.reshape(title_text)
        title_text_bidi = get_display(title_text_reshaped)

        # Set font and calculate position for the title
        pdf_canvas.setFont("IRANSansWeb", 24)
        title_width = pdf_canvas.stringWidth(title_text_bidi, "IRANSansWeb", 24)
        title_x = (width - title_width) / 2
        title_y = height - 50
        pdf_canvas.drawString(title_x, title_y, title_text_bidi)

        # Create the table header for the scores
        headers = ['ماه تحصیلی', 'نام دانش آموز', 'نمره دانش آموز', 'نام درس', 'ردیف']
        headers_reshaped = [get_display(arabic_reshaper.reshape(header)) for header in headers]
        data = [headers_reshaped]

        total_score = 0
        count_scores = len(context['user_info']['scores'])

        # Add each subject's scores into the table
        for index, score in enumerate(context['user_info']['scores']):
            data.append([
                get_display(arabic_reshaper.reshape(score['month'])),  # Month (آبان)
                get_display(arabic_reshaper.reshape(score['name'])),   # Student's name
                str(score['score']),  # Score
                get_display(arabic_reshaper.reshape(score['subject'])),  # Subject name
                str(index + 1),  # Row number
            ])
            total_score += float(score['score'])

        # Calculate the average score
        average_score = total_score / count_scores if count_scores > 0 else 0
        last_student_name = context['user_info']['scores'][-1]['name'] if count_scores > 0 else "ناشناس"

        # Add a row for the average score
        average_row = [
            get_display(arabic_reshaper.reshape("آبان")),  # Month (آبان)
            get_display(arabic_reshaper.reshape(last_student_name)),  # Last student's name
            f"{average_score:.2f}",  # Average score
            get_display(arabic_reshaper.reshape("میانگین")),  # "Average"
            str(count_scores + 1)  # Row number
        ]
        data.append(average_row)

        # Set column widths and row heights for the table
        col_widths = [100, 150, 100, 150, 60]  # Increased column widths for better spacing
        row_heights = [30] * (len(data) - 1) + [30]  # Increased row height

        # Create the table and apply styles
        table = Table(data, colWidths=col_widths, rowHeights=row_heights)
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'IRANSansWeb'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, len(data) - 1), (-1, len(data) - 1), colors.lightgrey),
            ('TEXTCOLOR', (0, len(data) - 1), (-1, len(data) - 1), colors.black),
            ('ALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'CENTER'),
            ('VALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'MIDDLE'),
        ]))

        # Calculate table position to center it on the page
        table_width, table_height = table.wrap(0, 0)
        table_x = (width - table_width) / 2
        table_y = title_y - 50 - table_height

        # Draw the table on the Canvas
        table.drawOn(pdf_canvas, table_x, table_y)

        # Add footer to the PDF
        footer_height = 30  # Footer height
        footer_y = 0  # Position the footer at the bottom of the page
        footer_text = "سامانه هوشمند استعداد های درخشان زنده یاد کردی ساخته شده توسط امیر حسین غلامی"
        footer_text_reshaped = arabic_reshaper.reshape(footer_text)
        footer_text_bidi = get_display(footer_text_reshaped)

        # Draw footer background and text
        pdf_canvas.setFillColor(colors.lightgrey)
        pdf_canvas.rect(0, footer_y, width, footer_height, fill=True, stroke=False)

        # Set font and position for footer text
        pdf_canvas.setFont("IRANSansWeb", 12)
        footer_text_width = pdf_canvas.stringWidth(footer_text_bidi, "IRANSansWeb", 12)
        footer_text_x = (width - footer_text_width) / 2
        footer_text_y = footer_y + 8
        pdf_canvas.setFillColor(colors.black)
        pdf_canvas.drawString(footer_text_x, footer_text_y, footer_text_bidi)

        # Save the PDF document
        pdf_canvas.save()
        return response

    def get(self, request, *args, **kwargs):
        """
        Retrieves the student data and generates the score report for "آبان" month.
        If requested, the report is generated in PDF format.
        """
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            # Get the subject scores and average score
            subject_scores, average_score = self.get_subject_scores(student_data.name, subject_models)

            # Prepare the context for rendering
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores,
                    'average_score': average_score
                }
            }

            # If PDF download is requested, generate the PDF
            if 'download_pdf' in request.GET:
                return self.generate_pdf(context)

            # Otherwise, render the scores in HTML
            return render(request, 'Student Page/Score/Aban.html', context)
        else:
            # Render error page if user is not found
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})


@method_decorator(login_required, name='dispatch')
class Student_Score_Azar(View):
    # Method to retrieve student data and subject mappings based on username
    def get_user_data(self, user):
        """
        Searches for the student's data across different models
        Returns the student data and corresponding subjects.
        """
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}  # Return None if student data is not found

    # Method to fetch subject scores for the student in Azar month
    def get_subject_scores(self, student_name, subject_models):
        """
        Collects the student's scores from different models, filtering for the month 'آذر'.
        """
        subject_scores = []  # List to store subject scores
        total_score = 0  # Total score for all subjects
        score_count = 0  # Count of subjects for averaging

        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='آذر')
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # Persian subject name
                    'name': score.name,  # Student name
                    'month': score.month,  # Month of the score
                    'score': score.score  # Actual score
                })
                total_score += float(score.score)
                score_count += 1  # Increment score count

        # Calculate average score
        average_score = total_score / score_count if score_count > 0 else 0
        return subject_scores, average_score

    # Method to generate the PDF report for the student scores
    def generate_pdf(self, context):
        """
        Generates and returns a PDF document with the student's scores for Azar.
        """
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="scores_azar.pdf"'

        # Create a canvas object to draw on the PDF
        pdf_canvas = canvas.Canvas(response, pagesize=letter)
        width, height = letter  # Page size

        # Register Persian font
        pdfmetrics.registerFont(TTFont('IRANSansWeb', 'static/Static Student/fonts/IRANSansWeb_Medium.ttf'))

        # Draw images for branding
        self.draw_images(pdf_canvas, width, height)

        # Add title to the document
        self.add_title(pdf_canvas, width, height)

        # Create and add the scores table to the PDF
        self.add_scores_table(pdf_canvas, context, width, height)

        # Add footer to the PDF
        self.add_footer(pdf_canvas, width)

        # Finalize and save the PDF
        pdf_canvas.save()
        return response

    def draw_images(self, pdf_canvas, width, height):
        """
        Draws the logo and the 'Iran Amozesho Parvaresh' image on the PDF.
        """
        image1_path = 'static/Static Student/images/Logo.png'
        image2_path = 'static/Static Student/images/Iran_AmozeshoParvaresh.png'
        pdf_canvas.drawImage(image1_path, 5, height - 98, width=100, height=100, mask='auto')
        pdf_canvas.drawImage(image2_path, 520, height - 95, width=90, height=90, mask='auto')

    def add_title(self, pdf_canvas, width, height):
        """
        Adds the Persian title 'کارنامه آذر ماه' to the PDF document.
        """
        title_text = "کارنامه آذر ماه"
        title_text_reshaped = arabic_reshaper.reshape(title_text)
        title_text_bidi = get_display(title_text_reshaped)

        # Set font and position for the title
        pdf_canvas.setFont("IRANSansWeb", 24)
        title_width = pdf_canvas.stringWidth(title_text_bidi, "IRANSansWeb", 24)
        title_x = (width - title_width) / 2
        title_y = height - 50
        pdf_canvas.drawString(title_x, title_y, title_text_bidi)

    def add_scores_table(self, pdf_canvas, context, width, height):
        """
        Creates and adds the table containing the student's scores to the PDF.
        """
        headers = ['ماه تحصیلی', 'نام دانش آموز', 'نمره دانش آموز', 'نام درس', 'ردیف']
        headers_reshaped = [get_display(arabic_reshaper.reshape(header)) for header in headers]
        data = [headers_reshaped]  # Start with headers

        total_score = 0
        count_scores = len(context['user_info']['scores'])

        # Add the student's scores row by row
        for index, score in enumerate(context['user_info']['scores']):
            data.append([
                get_display(arabic_reshaper.reshape(score['month'])),
                get_display(arabic_reshaper.reshape(score['name'])),
                str(score['score']),
                get_display(arabic_reshaper.reshape(score['subject'])),
                str(index + 1),
            ])
            total_score += float(score.score)  # Summing the scores

        # Calculate the average score
        average_score = total_score / count_scores if count_scores > 0 else 0
        last_student_name = context['user_info']['scores'][-1]['name'] if count_scores > 0 else "ناشناس"

        # Add the row for the average score
        average_row = [
            get_display(arabic_reshaper.reshape("آذر")),
            get_display(arabic_reshaper.reshape(last_student_name)),
            f"{average_score:.2f}",
            get_display(arabic_reshaper.reshape("میانگین")),
            str(count_scores + 1)
        ]
        data.append(average_row)

        # Set table styles
        table = Table(data, colWidths=[100, 150, 100, 150, 60], rowHeights=[30] * (len(data) - 1) + [30])
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'IRANSansWeb'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, len(data) - 1), (-1, len(data) - 1), colors.lightgrey),
            ('TEXTCOLOR', (0, len(data) - 1), (-1, len(data) - 1), colors.black),
            ('ALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'CENTER'),
            ('VALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'MIDDLE'),
        ]))

        # Calculate position for the table to center it on the page
        table_width, table_height = table.wrap(0, 0)
        table_x = (width - table_width) / 2
        table_y = height - 150 - table_height  # Adjusted for title space
        table.drawOn(pdf_canvas, table_x, table_y)

    def add_footer(self, pdf_canvas, width):
        """
        Adds a footer to the PDF document.
        """
        footer_height = 30
        footer_text = "سامانه هوشمند استعداد های درخشان زنده یاد کردی ساخته شده توسط امیر حسین غلامی"
        footer_text_reshaped = arabic_reshaper.reshape(footer_text)
        footer_text_bidi = get_display(footer_text_reshaped)

        # Draw footer background
        pdf_canvas.setFillColor(colors.lightgrey)
        pdf_canvas.rect(0, 0, width, footer_height, fill=True, stroke=False)

        # Add footer text
        pdf_canvas.setFont("IRANSansWeb", 12)
        footer_text_width = pdf_canvas.stringWidth(footer_text_bidi, "IRANSansWeb", 12)
        footer_text_x = (width - footer_text_width) / 2
        footer_text_y = 8
        pdf_canvas.setFillColor(colors.black)
        pdf_canvas.drawString(footer_text_x, footer_text_y, footer_text_bidi)

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to fetch and display or generate the PDF report.
        """
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            subject_scores, average_score = self.get_subject_scores(student_data.name, subject_models)

            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores,
                    'average_score': average_score
                }
            }

            if 'download_pdf' in request.GET:
                return self.generate_pdf(context)

            return render(request, 'Student Page/Score/Azar.html', context)
        else:
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})


@method_decorator(login_required, name='dispatch')
class Student_Score_Dey(View):

    def get_user_data(self, user):
        """
        Searches for the student's data in different models based on their username.
        Returns the student data and corresponding subjects.
        """
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}

    def get_subject_scores(self, student_name, subject_models):
        """
        Collects the student's scores from different models, filtering by the month "دی".
        Returns the subject scores and the calculated average score.
        """
        subject_scores = []
        total_score = 0
        score_count = 0

        # Iterate through the subjects and models to collect scores
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='دی')
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # Persian subject name
                    'name': score.name,
                    'month': score.month,
                    'score': score.score
                })
                total_score += score.score  # Add score to total
                score_count += 1  # Increment score count

        # Calculate the average score
        average_score = total_score / score_count if score_count > 0 else 0
        return subject_scores, average_score

    def generate_pdf(self, context):
        """
        Generates and returns a PDF document containing the student's scores for the month "دی".
        """
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="scores_dey.pdf"'

        # Create a canvas to generate the PDF
        pdf_canvas = canvas.Canvas(response, pagesize=letter)
        width, height = letter  # Set page size

        # Register Persian font
        pdfmetrics.registerFont(TTFont('IRANSansWeb', 'static/Static Student/fonts/IRANSansWeb_Medium.ttf'))

        # Add images (logo and Iranian education brand)
        image1_path = 'static/Static Student/images/Logo.png'
        image2_path = 'static/Static Student/images/Iran_AmozeshoParvaresh.png'
        pdf_canvas.drawImage(image1_path, 5, height - 98, width=100, height=100, mask='auto')
        pdf_canvas.drawImage(image2_path, 520, height - 95, width=90, height=90, mask='auto')

        # Add title "کارنامه دی ماه"
        title_text = "کارنامه دی ماه"
        title_text_reshaped = arabic_reshaper.reshape(title_text)
        title_text_bidi = get_display(title_text_reshaped)

        # Set font for the title
        pdf_canvas.setFont("IRANSansWeb", 24)
        title_width = pdf_canvas.stringWidth(title_text_bidi, "IRANSansWeb", 24)
        title_x = (width - title_width) / 2
        title_y = height - 50
        pdf_canvas.drawString(title_x, title_y, title_text_bidi)

        # Create table headers and reshaped them for bidi compatibility
        headers = ['ماه تحصیلی', 'نام دانش آموز', 'نمره دانش آموز', 'نام درس', 'ردیف']
        headers_reshaped = [get_display(arabic_reshaper.reshape(header)) for header in headers]
        data = [headers_reshaped]  # Initialize table with headers

        total_score = 0
        count_scores = len(context['user_info']['scores'])

        # Add student scores to the table
        for index, score in enumerate(context['user_info']['scores']):
            data.append([
                get_display(arabic_reshaper.reshape(score['month'])),
                get_display(arabic_reshaper.reshape(score['name'])),
                str(score['score']),
                get_display(arabic_reshaper.reshape(score['subject'])),
                str(index + 1),
            ])
            total_score += score['score']  # Sum the scores

        # Calculate the average score
        average_score = total_score / count_scores if count_scores > 0 else 0
        last_student_name = context['user_info']['scores'][-1]['name'] if count_scores > 0 else "ناشناس"

        # Add row for the average score
        average_row = [
            get_display(arabic_reshaper.reshape(score['month'])),
            get_display(arabic_reshaper.reshape(last_student_name)),
            f"{average_score:.2f}",
            get_display(arabic_reshaper.reshape("میانگین")),
            str(count_scores + 1)
        ]
        data.append(average_row)

        # Set column widths and row heights for a bigger table
        col_widths = [100, 150, 100, 150, 60]  # Larger column widths
        row_heights = [30] * (len(data) - 1) + [30]  # Larger row heights

        table = Table(data, colWidths=col_widths, rowHeights=row_heights)

        # Set table style
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'IRANSansWeb'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, len(data) - 1), (-1, len(data) - 1), colors.lightgrey),
            ('TEXTCOLOR', (0, len(data) - 1), (-1, len(data) - 1), colors.black),
            ('ALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'CENTER'),
            ('VALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'MIDDLE'),
        ]))

        # Calculate the table position to center it on the page
        table_width, table_height = table.wrap(0, 0)
        table_x = (width - table_width) / 2
        table_y = title_y - 50 - table_height  # Adjusted for title height

        # Draw the table
        table.drawOn(pdf_canvas, table_x, table_y)

        # Draw footer
        footer_height = 30
        footer_y = 0
        footer_text = "سامانه هوشمند استعداد های درخشان زنده یاد کردی ساخته شده توسط امیر حسین غلامی"
        footer_text_reshaped = arabic_reshaper.reshape(footer_text)
        footer_text_bidi = get_display(footer_text_reshaped)

        # Draw footer background
        pdf_canvas.setFillColor(colors.lightgrey)
        pdf_canvas.rect(0, footer_y, width, footer_height, fill=True, stroke=False)

        # Set footer font
        pdf_canvas.setFont("IRANSansWeb", 12)
        footer_text_width = pdf_canvas.stringWidth(footer_text_bidi, "IRANSansWeb", 12)
        footer_text_x = (width - footer_text_width) / 2
        footer_text_y = footer_y + 8
        pdf_canvas.setFillColor(colors.black)
        pdf_canvas.drawString(footer_text_x, footer_text_y, footer_text_bidi)

        # Save the PDF document
        pdf_canvas.save()
        return response

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to fetch and display the scores or generate a PDF.
        """
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            subject_scores, average_score = self.get_subject_scores(student_data.name, subject_models)

            # Prepare context data to send to the template
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores,
                    'average_score': average_score  # Include average score in context
                }
            }

            # Check if the user requested a PDF download
            if 'download_pdf' in request.GET:
                return self.generate_pdf(context)

            return render(request, 'Student Page/Score/Dey.html', context)
        else:
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})


# A decorator that ensures the user is logged in before accessing the page
@method_decorator(login_required, name='dispatch')
class Student_Score_Bahman(View):

    # Method to fetch student data and their corresponding subjects
    def get_user_data(self, user):
        # Searching for student data in different models
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}  # Return None if no student data is found

    # Method to fetch the subject scores for the student for the month 'بهمن'
    def get_subject_scores(self, student_name, subject_models):
        subject_scores = []  # List to store scores
        total_score = 0  # Total score accumulator
        score_count = 0  # To count the number of scores

        # Loop through subject models to fetch scores for the month 'بهمن'
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='بهمن')
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # The subject name in Persian
                    'name': score.name,
                    'month': score.month,
                    'score': score.score
                })
                total_score += score.score  # Accumulate total score
                score_count += 1  # Increment the score count

        # Calculate the average score, return 0 if no scores are found
        average_score = total_score / score_count if score_count > 0 else 0
        return subject_scores, average_score

    # Method to generate the PDF report
    def generate_pdf(self, context):
        # Response for the PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="scores_bahman.pdf"'

        # Create PDF canvas
        pdf_canvas = canvas.Canvas(response, pagesize=letter)
        width, height = letter  # Page dimensions

        # Register and load Persian font
        pdfmetrics.registerFont(TTFont('IRANSansWeb', 'static/Static Student/fonts/IRANSansWeb_Medium.ttf'))

        # Paths for the images to be added in the PDF
        image1_path = 'static/Static Student/images/Logo.png'
        image2_path = 'static/Static Student/images/Iran_AmozeshoParvaresh.png'

        # Add first image (Logo)
        pdf_canvas.drawImage(image1_path, 5, height - 98, width=100, height=100, mask='auto')
        # Add second image (Iran Education Logo)
        pdf_canvas.drawImage(image2_path, 520, height - 95, width=90, height=90, mask='auto')

        # Add title in Persian
        title_text = "کارنامه بهمن ماه"
        title_text_reshaped = arabic_reshaper.reshape(title_text)
        title_text_bidi = get_display(title_text_reshaped)

        # Set font and size for the title
        pdf_canvas.setFont("IRANSansWeb", 24)
        title_width = pdf_canvas.stringWidth(title_text_bidi, "IRANSansWeb", 24)
        title_x = (width - title_width) / 2
        title_y = height - 50
        pdf_canvas.drawString(title_x, title_y, title_text_bidi)

        # Create table headers in Persian
        headers = ['ماه تحصیلی', 'نام دانش آموز', 'نمره دانش آموز', 'نام درس', 'ردیف']
        headers_reshaped = [get_display(arabic_reshaper.reshape(header)) for header in headers]
        data = [headers_reshaped]  # Table data

        # Initialize the total score accumulator and the number of scores
        total_score = 0
        count_scores = len(context['user_info']['scores'])

        # Add student scores data into the table
        for index, score in enumerate(context['user_info']['scores']):
            data.append([
                get_display(arabic_reshaper.reshape(score['month'])),
                get_display(arabic_reshaper.reshape(score['name'])),
                str(score['score']),
                get_display(arabic_reshaper.reshape(score['subject'])),
                str(index + 1),
            ])
            total_score += score['score']

        # Calculate the average score for the student
        average_score = total_score / count_scores if count_scores > 0 else 0
        last_student_name = context['user_info']['scores'][-1]['name'] if count_scores > 0 else "ناشناس"

        # Add average row at the bottom of the table
        average_row = [
            get_display(arabic_reshaper.reshape(score['month'])),
            get_display(arabic_reshaper.reshape(last_student_name)),
            f"{average_score:.2f}",
            get_display(arabic_reshaper.reshape("میانگین")),
            str(count_scores + 1)
        ]
        data.append(average_row)

        # Define column widths and row heights
        col_widths = [100, 150, 100, 150, 60]  # Wider columns
        row_heights = [30] * (len(data) - 1) + [30]  # Table row heights

        # Create the table in the PDF
        table = Table(data, colWidths=col_widths, rowHeights=row_heights)

        # Apply table styling
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'IRANSansWeb'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, len(data) - 1), (-1, len(data) - 1), colors.lightgrey),
            ('TEXTCOLOR', (0, len(data) - 1), (-1, len(data) - 1), colors.black),
            ('ALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'CENTER'),
            ('VALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'MIDDLE'),
        ]))

        # Calculate table position to center it on the page
        table_width, table_height = table.wrap(0, 0)
        table_x = (width - table_width) / 2
        table_y = title_y - 50 - table_height

        # Draw the table on the PDF
        table.drawOn(pdf_canvas, table_x, table_y)

        # Add footer
        footer_height = 30
        footer_y = 0
        footer_text = "سامانه هوشمند استعداد های درخشان زنده یاد کردی ساخته شده توسط امیر حسین غلامی"
        footer_text_reshaped = arabic_reshaper.reshape(footer_text)
        footer_text_bidi = get_display(footer_text_reshaped)

        # Draw footer background
        pdf_canvas.setFillColor(colors.lightgrey)
        pdf_canvas.rect(0, footer_y, width, footer_height, fill=True, stroke=False)

        # Set footer font and draw it
        pdf_canvas.setFont("IRANSansWeb", 12)
        footer_text_width = pdf_canvas.stringWidth(footer_text_bidi, "IRANSansWeb", 12)
        footer_text_x = (width - footer_text_width) / 2
        footer_text_y = footer_y + 8
        pdf_canvas.setFillColor(colors.black)
        pdf_canvas.drawString(footer_text_x, footer_text_y, footer_text_bidi)

        # Save the PDF
        pdf_canvas.save()
        return response

    # GET request handler
    def get(self, request, *args, **kwargs):
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            # Fetch the student's scores and average score
            subject_scores, average_score = self.get_subject_scores(student_data.name, subject_models)

            # Prepare context for rendering the page
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores,
                    'average_score': average_score  # Include the average score
                }
            }

            # Check if the user wants to download the PDF
            if 'download_pdf' in request.GET:
                return self.generate_pdf(context)

            # Render the template if not requesting a PDF
            return render(request, 'Student Page/Score/Bahman.html', context)
        else:
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})  # User not found error


# Ensure that the user is logged in before accessing this view
@method_decorator(login_required, name='dispatch')
class Student_Score_Esfand(View):

    # Method to fetch the student data from models
    def get_user_data(self, user):
        # جستجوی اطلاعات دانش‌آموز در مدل‌های مختلف
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}  # Return None if no student data is found

    # Method to fetch scores of the student for the month "اسفند"
    def get_subject_scores(self, student_name, subject_models):
        subject_scores = []  # List to store the subject scores
        total_score = 0  # Variable to accumulate total score
        score_count = 0  # To count the number of scores

        # جمع‌آوری نمرات دانش‌آموز از مدل‌های مختلف و فیلتر کردن بر اساس ماه "اسفند"
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='اسفند')
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # نام درس به فارسی
                    'name': score.name,
                    'month': score.month,
                    'score': score.score
                })
                total_score += score.score
                score_count += 1

        # محاسبه میانگین نمرات
        average_score = total_score / score_count if score_count > 0 else 0
        return subject_scores, average_score

    # Method to generate the PDF report
    def generate_pdf(self, context):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="scores_esfand.pdf"'

        # Create PDF Canvas
        pdf_canvas = canvas.Canvas(response, pagesize=letter)
        width, height = letter  # Page dimensions

        # Register Persian font
        pdfmetrics.registerFont(TTFont('IRANSansWeb', 'static/Static Student/fonts/IRANSansWeb_Medium.ttf'))

        # Paths to images
        image1_path = 'static/Static Student/images/Logo.png'
        image2_path = 'static/Static Student/images/Iran_AmozeshoParvaresh.png'

        # Add images to PDF
        pdf_canvas.drawImage(image1_path, 5, height - 98, width=100, height=100, mask='auto')  # First image (Logo)
        pdf_canvas.drawImage(image2_path, 520, height - 95, width=90, height=90, mask='auto')  # Second image

        # Add title in Persian
        title_text = "کارنامه اسفند ماه"
        title_text_reshaped = arabic_reshaper.reshape(title_text)
        title_text_bidi = get_display(title_text_reshaped)

        # Set font for title and position it in the center
        pdf_canvas.setFont("IRANSansWeb", 24)
        title_width = pdf_canvas.stringWidth(title_text_bidi, "IRANSansWeb", 24)
        title_x = (width - title_width) / 2
        title_y = height - 50
        pdf_canvas.drawString(title_x, title_y, title_text_bidi)

        # Create table headers in Persian
        headers = ['ماه تحصیلی', 'نام دانش آموز', 'نمره دانش آموز', 'نام درس', 'ردیف']
        headers_reshaped = [get_display(arabic_reshaper.reshape(header)) for header in headers]
        data = [headers_reshaped]  # Table data

        total_score = 0  # Initialize total score for the table
        count_scores = len(context['user_info']['scores'])  # Count the number of scores

        # Add the student scores to the table
        for index, score in enumerate(context['user_info']['scores']):
            data.append([
                get_display(arabic_reshaper.reshape(score['month'])),
                get_display(arabic_reshaper.reshape(score['name'])),
                str(score['score']),
                get_display(arabic_reshaper.reshape(score['subject'])),
                str(index + 1),
            ])
            total_score += score['score']  # Add score to total score

        # Calculate average score
        average_score = total_score / count_scores if count_scores > 0 else 0
        last_student_name = context['user_info']['scores'][-1]['name'] if count_scores > 0 else "ناشناس"

        # Add average row at the bottom of the table
        average_row = [
            get_display(arabic_reshaper.reshape(score['month'])),
            get_display(arabic_reshaper.reshape(last_student_name)),
            f"{average_score:.2f}",
            get_display(arabic_reshaper.reshape("میانگین")),
            str(count_scores + 1)
        ]
        data.append(average_row)

        # Define column widths and row heights for the table
        col_widths = [100, 150, 100, 150, 60]  # Wider columns for better spacing
        row_heights = [30] * (len(data) - 1) + [30]  # Uniform row height

        # Create the table
        table = Table(data, colWidths=col_widths, rowHeights=row_heights)

        # Apply table styling
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'IRANSansWeb'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, len(data) - 1), (-1, len(data) - 1), colors.lightgrey),
            ('TEXTCOLOR', (0, len(data) - 1), (-1, len(data) - 1), colors.black),
            ('ALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'CENTER'),
            ('VALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'MIDDLE'),
        ]))

        # Calculate table position to center it on the page
        table_width, table_height = table.wrap(0, 0)
        table_x = (width - table_width) / 2
        table_y = title_y - 50 - table_height

        # Draw the table on the PDF
        table.drawOn(pdf_canvas, table_x, table_y)

        # Add footer
        footer_height = 30
        footer_y = 0
        footer_text = "سامانه هوشمند استعداد های درخشان زنده یاد کردی ساخته شده توسط امیر حسین غلامی"
        footer_text_reshaped = arabic_reshaper.reshape(footer_text)
        footer_text_bidi = get_display(footer_text_reshaped)

        # Draw footer background
        pdf_canvas.setFillColor(colors.lightgrey)
        pdf_canvas.rect(0, footer_y, width, footer_height, fill=True, stroke=False)

        # Set footer font and draw the footer text
        pdf_canvas.setFont("IRANSansWeb", 12)
        footer_text_width = pdf_canvas.stringWidth(footer_text_bidi, "IRANSansWeb", 12)
        footer_text_x = (width - footer_text_width) / 2
        footer_text_y = footer_y + 8
        pdf_canvas.setFillColor(colors.black)
        pdf_canvas.drawString(footer_text_x, footer_text_y, footer_text_bidi)

        # Save and close the PDF file
        pdf_canvas.save()
        return response

    # GET request handler
    def get(self, request, *args, **kwargs):
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            # Fetch the student's scores and calculate the average
            subject_scores, average_score = self.get_subject_scores(student_data.name, subject_models)

            # Prepare context for rendering the template
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores,
                    'average_score': average_score  # Include the average score
                }
            }

            # Check if the user requested to download the PDF
            if 'download_pdf' in request.GET:
                return self.generate_pdf(context)

            # Render the template if not requesting a PDF
            return render(request, 'Student Page/Score/Esfand.html', context)
        else:
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})  # User not found error


# Decorator to ensure the user is logged in before accessing the view
@method_decorator(login_required, name='dispatch')
class Student_Score_Farvardin(View):
    
    def get_user_data(self, user):
        """
        Retrieve the student data from different models based on the username.
        Returns the student data and associated subjects if found, otherwise returns None.
        """
        # Loop through predefined student models to find data based on username
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}

    def get_subject_scores(self, student_name, subject_models):
        """
        Collect the student's scores for the month 'Farvardin' from the different subject models.
        Calculates the total score and average score.
        """
        subject_scores = []  # List to hold subject scores
        total_score = 0  # Variable to accumulate total score
        score_count = 0  # Count of scores to calculate the average

        # Iterate through each subject model to fetch the student's scores
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='فروردین')  # Filter by name and month
            for score in scores:
                # Append each score to the subject_scores list with its details
                subject_scores.append({
                    'subject': subject_name,  # Subject name in Persian
                    'name': score.name,
                    'month': score.month,
                    'score': score.score
                })
                total_score += score.score  # Add the score to the total score
                score_count += 1  # Increment the score count

        # Calculate average score if there are scores
        average_score = total_score / score_count if score_count > 0 else 0
        return subject_scores, average_score

    def generate_pdf(self, context):
        """
        Generates a PDF document containing the student's score report for Farvardin.
        """
        # Create an HTTP response with PDF content type
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="scores_farvardin.pdf"'

        # Create a PDF canvas
        pdf_canvas = canvas.Canvas(response, pagesize=letter)
        width, height = letter  # Page size dimensions

        # Register Persian font for the PDF
        pdfmetrics.registerFont(TTFont('IRANSansWeb', 'static/Static Student/fonts/IRANSansWeb_Medium.ttf'))

        # Add images to the PDF (Logo and other image)
        image1_path = 'static/Static Student/images/Logo.png'
        image2_path = 'static/Static Student/images/Iran_AmozeshoParvaresh.png'

        # Draw the images on the canvas
        pdf_canvas.drawImage(image1_path, 5, height - 98, width=100, height=100, mask='auto')
        pdf_canvas.drawImage(image2_path, 520, height - 95, width=90, height=90, mask='auto')

        # Add title to the PDF (Persian text)
        title_text = "کارنامه فروردین ماه"
        title_text_reshaped = arabic_reshaper.reshape(title_text)  # Reshape Persian text for proper display
        title_text_bidi = get_display(title_text_reshaped)  # Apply bidirectional display

        # Set font and size for the title
        pdf_canvas.setFont("IRANSansWeb", 24)
        title_width = pdf_canvas.stringWidth(title_text_bidi, "IRANSansWeb", 24)
        title_x = (width - title_width) / 2  # Center the title
        title_y = height - 50
        pdf_canvas.drawString(title_x, title_y, title_text_bidi)

        # Prepare table headers
        headers = ['ماه تحصیلی', 'نام دانش آموز', 'نمره دانش آموز', 'نام درس', 'ردیف']
        headers_reshaped = [get_display(arabic_reshaper.reshape(header)) for header in headers]
        data = [headers_reshaped]  # Initialize the table with headers

        total_score = 0  # Total score for all subjects
        count_scores = len(context['user_info']['scores'])  # Number of scores

        # Add the scores to the table
        for index, score in enumerate(context['user_info']['scores']):
            data.append([
                get_display(arabic_reshaper.reshape(score['month'])),
                get_display(arabic_reshaper.reshape(score['name'])),
                str(score['score']),
                get_display(arabic_reshaper.reshape(score['subject'])),
                str(index + 1),
            ])
            total_score += score['score']  # Add score to total

        # Calculate average score
        average_score = total_score / count_scores if count_scores > 0 else 0
        last_student_name = context['user_info']['scores'][-1]['name'] if count_scores > 0 else "ناشناس"

        # Add average score row to the table
        average_row = [
            get_display(arabic_reshaper.reshape("فروردین")),
            get_display(arabic_reshaper.reshape(last_student_name)),
            f"{average_score:.2f}",
            get_display(arabic_reshaper.reshape("میانگین")),
            str(count_scores + 1)
        ]
        data.append(average_row)

        # Set column widths and row heights for the table
        col_widths = [100, 150, 100, 150, 60]  # Adjust column widths for readability
        row_heights = [30] * (len(data) - 1) + [30]  # Set height for each row

        # Create a table with the data
        table = Table(data, colWidths=col_widths, rowHeights=row_heights)

        # Apply table styles
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'IRANSansWeb'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, len(data) - 1), (-1, len(data) - 1), colors.lightgrey),
            ('TEXTCOLOR', (0, len(data) - 1), (-1, len(data) - 1), colors.black),
            ('ALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'CENTER'),
            ('VALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'MIDDLE'),
        ]))

        # Calculate table position to center it on the page
        table_width, table_height = table.wrap(0, 0)
        table_x = (width - table_width) / 2
        table_y = title_y - 50 - table_height

        # Draw the table on the canvas
        table.drawOn(pdf_canvas, table_x, table_y)

        # Add footer to the PDF
        footer_height = 30
        footer_y = 0
        footer_text = "سامانه هوشمند استعداد های درخشان زنده یاد کردی ساخته شده توسط امیر حسین غلامی"
        footer_text_reshaped = arabic_reshaper.reshape(footer_text)
        footer_text_bidi = get_display(footer_text_reshaped)

        # Draw footer background
        pdf_canvas.setFillColor(colors.lightgrey)
        pdf_canvas.rect(0, footer_y, width, footer_height, fill=True, stroke=False)

        # Set footer font and draw text
        pdf_canvas.setFont("IRANSansWeb", 12)
        footer_text_width = pdf_canvas.stringWidth(footer_text_bidi, "IRANSansWeb", 12)
        footer_text_x = (width - footer_text_width) / 2
        footer_text_y = footer_y + 8
        pdf_canvas.setFillColor(colors.black)
        pdf_canvas.drawString(footer_text_x, footer_text_y, footer_text_bidi)

        # Finalize the PDF document
        pdf_canvas.save()
        return response

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests: Retrieve the student's scores for Farvardin,
        and optionally generate a PDF if requested.
        """
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            # Get the subject scores and calculate the average
            subject_scores, average_score = self.get_subject_scores(student_data.name, subject_models)

            # Prepare context for rendering the HTML or PDF
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores,
                    'average_score': average_score  # Include the average score
                }
            }

            # Check if the user has requested a PDF download
            if 'download_pdf' in request.GET:
                return self.generate_pdf(context)

            # Render the HTML template with the student's data
            return render(request, 'Student Page/Score/Farvardin.html', context)
        else:
            # If student data is not found, return an error message
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})


# Ensure the user is logged in before accessing the view
@method_decorator(login_required, name='dispatch')
class Student_Score_Ordibeheshet(View):

    def get_user_data(self, user):
        """
        Retrieve student data from the corresponding model based on the username.
        Returns student data and subject models if found, otherwise returns None.
        """
        # Iterate through predefined student models to find the data based on username
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}

    def get_subject_scores(self, student_name, subject_models):
        """
        Collect the student's scores for the month 'Ordibeheshet' from various subject models.
        Also calculates the total score and average score.
        """
        subject_scores = []  # List to hold the subject scores
        total_score = 0  # Variable to accumulate the total score
        score_count = 0  # Count of scores to calculate the average

        # Loop through each subject model to fetch the student's scores
        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='اردیبهشت')  # Filter by name and month
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # Subject name in Persian
                    'name': score.name,
                    'month': score.month,
                    'score': score.score
                })
                total_score += score.score  # Add the score to total score
                score_count += 1  # Increment score count

        # Calculate the average score if there are scores available
        average_score = total_score / score_count if score_count > 0 else 0
        return subject_scores, average_score

    def generate_pdf(self, context):
        """
        Generates a PDF document containing the student's score report for Ordibeheshet.
        """
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="scores_ordibeheshet.pdf"'

        # Create a PDF canvas
        pdf_canvas = canvas.Canvas(response, pagesize=letter)
        width, height = letter  # Page size dimensions

        # Register Persian font for the PDF
        pdfmetrics.registerFont(TTFont('IRANSansWeb', 'static/Static Student/fonts/IRANSansWeb_Medium.ttf'))

        # Add images (Logo and other image)
        image1_path = 'static/Static Student/images/Logo.png'
        image2_path = 'static/Static Student/images/Iran_AmozeshoParvaresh.png'

        # Draw the first image
        pdf_canvas.drawImage(image1_path, 5, height - 98, width=100, height=100, mask='auto')
        # Draw the second image
        pdf_canvas.drawImage(image2_path, 520, height - 95, width=90, height=90, mask='auto')

        # Add title (Persian text)
        title_text = "کارنامه اردیبهشت ماه"
        title_text_reshaped = arabic_reshaper.reshape(title_text)
        title_text_bidi = get_display(title_text_reshaped)

        # Set font and size for the title
        pdf_canvas.setFont("IRANSansWeb", 24)
        title_width = pdf_canvas.stringWidth(title_text_bidi, "IRANSansWeb", 24)
        title_x = (width - title_width) / 2  # Center the title
        title_y = height - 50
        pdf_canvas.drawString(title_x, title_y, title_text_bidi)

        # Prepare table headers (Persian text)
        headers = ['ماه تحصیلی', 'نام دانش آموز', 'نمره دانش آموز', 'نام درس', 'ردیف']
        headers_reshaped = [get_display(arabic_reshaper.reshape(header)) for header in headers]
        data = [headers_reshaped]  # Initialize the table with headers

        total_score = 0  # Total score across all subjects
        count_scores = len(context['user_info']['scores'])  # Number of scores

        # Add the subject scores to the table
        for index, score in enumerate(context['user_info']['scores']):
            data.append([
                get_display(arabic_reshaper.reshape(score['month'])),
                get_display(arabic_reshaper.reshape(score['name'])),
                str(score['score']),
                get_display(arabic_reshaper.reshape(score['subject'])),
                str(index + 1),
            ])
            total_score += score['score']  # Add score to total

        # Calculate average score
        average_score = total_score / count_scores if count_scores > 0 else 0
        last_student_name = context['user_info']['scores'][-1]['name'] if count_scores > 0 else "ناشناس"

        # Add average score row to the table
        average_row = [
            get_display(arabic_reshaper.reshape("اردیبهشت")),
            get_display(arabic_reshaper.reshape(last_student_name)),
            f"{average_score:.2f}",
            get_display(arabic_reshaper.reshape("میانگین")),
            str(count_scores + 1)
        ]
        data.append(average_row)

        # Set column widths and row heights for the table
        col_widths = [100, 150, 100, 150, 60]  # Adjust column widths for readability
        row_heights = [30] * (len(data) - 1) + [30]  # Set height for each row

        # Create a table with the data
        table = Table(data, colWidths=col_widths, rowHeights=row_heights)

        # Apply styles to the table
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'IRANSansWeb'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 5),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, len(data) - 1), (-1, len(data) - 1), colors.lightgrey),
            ('TEXTCOLOR', (0, len(data) - 1), (-1, len(data) - 1), colors.black),
            ('ALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'CENTER'),
            ('VALIGN', (0, len(data) - 1), (-1, len(data) - 1), 'MIDDLE'),
        ]))

        # Calculate the position to center the table on the page
        table_width, table_height = table.wrap(0, 0)
        table_x = (width - table_width) / 2
        table_y = title_y - 50 - table_height

        # Draw the table on the canvas
        table.drawOn(pdf_canvas, table_x, table_y)

        # Add footer to the PDF
        footer_height = 30
        footer_y = 0
        footer_text = "سامانه هوشمند استعداد های درخشان زنده یاد کردی ساخته شده توسط امیر حسین غلامی"
        footer_text_reshaped = arabic_reshaper.reshape(footer_text)
        footer_text_bidi = get_display(footer_text_reshaped)

        # Draw footer background
        pdf_canvas.setFillColor(colors.lightgrey)
        pdf_canvas.rect(0, footer_y, width, footer_height, fill=True, stroke=False)

        # Set footer font and draw the text
        pdf_canvas.setFont("IRANSansWeb", 12)
        footer_text_width = pdf_canvas.stringWidth(footer_text_bidi, "IRANSansWeb", 12)
        footer_text_x = (width - footer_text_width) / 2
        footer_text_y = footer_y + 8
        pdf_canvas.setFillColor(colors.black)
        pdf_canvas.drawString(footer_text_x, footer_text_y, footer_text_bidi)

        # Save the PDF document
        pdf_canvas.save()
        return response

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests: Retrieve the student's scores for Ordibeheshet,
        and optionally generate a PDF if requested.
        """
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            # Get subject scores and calculate the average score
            subject_scores, average_score = self.get_subject_scores(student_data.name, subject_models)

            # Prepare context for rendering the HTML or PDF
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores,
                    'average_score': average_score  # Include the average score
                }
            }

            # If a PDF download is requested
            if 'download_pdf' in request.GET:
                return self.generate_pdf(context)

            # Render the HTML template with the student's data
            return render(request, 'Student Page/Score/Ordibeheshet.html', context)
        else:
            # If no student data is found, show an error message
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})


# Apply login required decorator to the entire class to ensure user is logged in
@method_decorator(login_required, name='dispatch')
class Student_Score_Khordad(View):

    # Method to fetch the user data from different student models
    def get_user_data(self, user):
        """
        Search for student information across different models and 
        return the data along with the subjects they are enrolled in.
        """
        for student_model, subjects in STUDENT_MODEL_MAPPINGS.items():
            if student_model.objects.filter(username=user.username).exists():
                student_data = student_model.objects.get(username=user.username)
                return student_data, subjects
        return None, {}

    # Method to collect subject scores for a specific student and the "خرداد" month
    def get_subject_scores(self, student_name, subject_models):
        """
        Collect student scores from the models filtered by the month 'خرداد'.
        Also calculates the average score for the student.
        """
        subject_scores = []
        total_score = 0
        score_count = 0

        for model, subject_name in subject_models.items():
            scores = model.objects.filter(name=student_name, month='خرداد')
            for score in scores:
                subject_scores.append({
                    'subject': subject_name,  # Subject name in Persian
                    'name': score.name,
                    'month': score.month,
                    'score': score.score
                })
                total_score += score.score
                score_count += 1

        # Calculate the average score
        average_score = total_score / score_count if score_count > 0 else 0
        return subject_scores, average_score

    # Method to generate the PDF report for the student's scores
    def generate_pdf(self, context):
        """
        Generates a PDF report for the student's scores in the month of 'خرداد'.
        Includes a title, a table with the student's scores, and a footer.
        """
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="scores_khordad.pdf"'

        # Create a PDF canvas and set the page size to letter
        pdf_canvas = canvas.Canvas(response, pagesize=letter)
        width, height = letter

        # Load the Persian font for the report
        pdfmetrics.registerFont(TTFont('IRANSansWeb', 'static/Static Student/fonts/IRANSansWeb_Medium.ttf'))

        # Title of the report
        title_text = "کارنامه خرداد ماه"
        title_text_reshaped = arabic_reshaper.reshape(title_text)
        title_text_bidi = get_display(title_text_reshaped)

        # Set the font for the title and position it in the center
        pdf_canvas.setFont("IRANSansWeb", 24)
        title_width = pdf_canvas.stringWidth(title_text_bidi, "IRANSansWeb", 24)
        title_x = (width - title_width) / 2
        title_y = height - 50
        pdf_canvas.drawString(title_x, title_y, title_text_bidi)

        # Set up table headers for the student score data
        headers = ['ماه تحصیلی', 'نام دانش آموز', 'نمره دانش آموز', 'نام درس', 'ردیف']
        headers_reshaped = [get_display(arabic_reshaper.reshape(header)) for header in headers]
        data = [headers_reshaped]

        total_score = 0
        count_scores = len(context['user_info']['scores'])

        # Adding the student's scores to the table
        for index, score in enumerate(context['user_info']['scores']):
            data.append([
                get_display(arabic_reshaper.reshape(score['month'])),  # Month
                get_display(arabic_reshaper.reshape(score['name'])),  # Student name
                str(score['score']),  # Score
                get_display(arabic_reshaper.reshape(score['subject'])),  # Subject name
                str(index + 1),  # Row number
            ])
            total_score += score['score']

        # Calculate the average score for the student
        average_score = total_score / count_scores if count_scores > 0 else 0
        last_student_name = context['user_info']['scores'][-1]['name'] if count_scores > 0 else "ناشناس"

        # Add the average score row to the table
        average_row = [
            get_display(arabic_reshaper.reshape(score['month'])),
            get_display(arabic_reshaper.reshape(last_student_name)),
            f"{average_score:.2f}",
            get_display(arabic_reshaper.reshape("میانگین")),
            str(count_scores + 1)
        ]
        data.append(average_row)

        # Column widths and row heights for the table
        col_widths = [100, 150, 100, 150, 60]
        row_heights = [30] * (len(data) - 1) + [30]

        # Create the table and apply styles
        table = Table(data, colWidths=col_widths, rowHeights=row_heights)

        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'IRANSansWeb'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center-align text
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertical center alignment
            ('TOPPADDING', (0, 0), (-1, -1), 5),  # Padding for table rows
            ('BOTTOMPADDING', (0, 0), (-1, 0), 6),  # Padding for table headers
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Row background color
            ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grid lines around the table
            ('BACKGROUND', (0, len(data) - 1), (-1, len(data) - 1), colors.lightgrey),  # Average row color
            ('TEXTCOLOR', (0, len(data) - 1), (-1, len(data) - 1), colors.black),  # Average row text color
        ]))

        # Calculate the position to center the table on the page
        table_width, table_height = table.wrap(0, 0)
        table_x = (width - table_width) / 2
        table_y = title_y - 50 - table_height
        table.drawOn(pdf_canvas, table_x, table_y)

        # Footer text
        footer_text = "سامانه هوشمند استعداد های درخشان زنده یاد کردی ساخته شده توسط امیر حسین غلامی"
        footer_text_reshaped = arabic_reshaper.reshape(footer_text)
        footer_text_bidi = get_display(footer_text_reshaped)
        pdf_canvas.setFont("IRANSansWeb", 12)
        footer_text_width = pdf_canvas.stringWidth(footer_text_bidi, "IRANSansWeb", 12)
        footer_text_x = (width - footer_text_width) / 2
        pdf_canvas.drawString(footer_text_x, 10, footer_text_bidi)

        # Save the PDF and return it as a response
        pdf_canvas.save()
        return response

    # Main method to handle the GET request and render either PDF or HTML page
    def get(self, request, *args, **kwargs):
        user = request.user
        student_data, subject_models = self.get_user_data(user)

        if student_data:
            # Get the scores for the student
            subject_scores, average_score = self.get_subject_scores(student_data.name, subject_models)

            # Prepare context data for rendering the page or PDF
            context = {
                'user_info': {
                    'name': student_data.name,
                    'photo': student_data.photo.url if student_data.photo else None,
                    'scores': subject_scores,
                    'average_score': average_score
                }
            }

            # If a PDF is requested, generate and return it
            if 'download_pdf' in request.GET:
                return self.generate_pdf(context)

            # Otherwise, render the HTML page with the student's information
            return render(request, 'Student Page/Score/Khordad.html', context)
        else:
            # If no student data is found, show an error page
            return render(request, 'user_info.html', {'error': 'کاربر یافت نشد'})
        



class ChangeUP(LoginRequiredMixin, View):
    # List of student models to search through
    student_models = [
        Seven_Student_One, Seven_Student_Two, Eight_Student_One,
        Eight_Student_Two, Nine_Student_One, Nine_Student_Two
    ]

    def get_student(self, user):
        """
        Search for the student in multiple models based on the username.
        Iterates through the predefined student models and returns
        the student object if found, otherwise returns None.
        """
        for model in self.student_models:
            try:
                # Attempt to fetch the student object based on the username
                return model.objects.get(username=user.username)
            except model.DoesNotExist:
                # If the student is not found in this model, continue to the next model
                continue
        return None  # If no student is found, return None

    def get(self, request):
        """
        Handle GET request to render the student's current information.
        Retrieves the student object and passes it to the template context.
        """
        student = self.get_student(request.user)

        context = {
            'student': student  # Pass the student object to the template context
        }
        return render(request, 'Student Page/Change/index.html', context)

    def post(self, request):
        """
        Handle POST request to update the student's information.
        This includes updating the username, password, and photo.
        """
        student = self.get_student(request.user)  # Retrieve the student object

        if student:
            # Update username
            new_username = request.POST.get('username')
            if new_username:
                # Check if the new username is already taken
                if User.objects.filter(username=new_username).exists():
                    messages.error(request, "نام کاربری وارد شده تکراری است. لطفاً نام کاربری دیگری انتخاب کنید.")
                    return redirect('Change Page')  # Redirect back if the username is taken

                # Update the username in the auth_user model (Django's built-in user model)
                user = User.objects.get(username=student.username)
                user.username = new_username
                user.save()

                # Also update the username in the custom student model
                student.username = new_username

            # Update password
            new_password = request.POST.get('password')
            if new_password:
                # Set the new password securely using set_password (for hashing)
                user = User.objects.get(username=student.username)
                user.set_password(new_password)
                user.save()

                # If needed, update the password in the student model (be cautious with saving passwords)
                student.password = new_password
                student.save()

            # Update the photo
            new_photo = request.FILES.get('photo')
            if new_photo:
                student.photo = new_photo  # Update the student's photo

            student.save()  # Save all changes to the student model

            # Redirect back to the same page after successful updates
            return redirect('Change Page')

        # If the student is not found, redirect to the change page
        return redirect('Change Page')