from django.views.generic import TemplateView
from Service.models import Service
from django.shortcuts import redirect
from common.forms import Common_Form
from Staff.models import Staff
from Facilities.models import Facilities

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = Service.objects.all()
        context['facilities'] = Facilities.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        common = Common_Form(request.POST, request.FILES)
        context = super().get_context_data(**kwargs)

        if common.is_valid():
            common.save()
            return redirect("Home Page")
        else:
            return self.render_to_response(self.get_context_data(context=context))

        return self.render_to_response(self.get_context_data(context=context))


class AboutView(TemplateView):
    template_name = "About School Page/index.html"