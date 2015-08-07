from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class BaseView(TemplateView):
    template_name = 'backend/base.html'
    context = {

    }


class HomeView(BaseView):
    def get(self, request):
        return render(request, self.template_name, self.context)
