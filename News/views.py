from django.views.generic import TemplateView
from .models import News

class News_View(TemplateView):
    template_name = 'News Page/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Order by the 'id' field in descending order to show the latest first
        context['News'] = News.objects.order_by('-id')
        return context