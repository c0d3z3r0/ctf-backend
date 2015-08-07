from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class BaseView(TemplateView):
    template_name = 'backend/base.html'
    context = {
        'sitename': 'CTF@HSO',
    }


class HomeView(BaseView):
    def get(self, request):
        self.context.update(
            {
                'title':    'Welcome to CTF@HSO ...',
                'lead':     '... the Capture the Flag Workshop of the<br>'
                            'University of Applied Sciences in Offenburg.',
            }
        )
        return render(request, self.template_name, self.context)


# def home(request):
#     context = {
#         'sitename': 'CTF@HSO',
#         'title':    'Welcome to CTF@HSO ...',
#         'lead':     '... the Capture the Flag Workshop of the<br>'
#                     'University of Applied Sciences in Offenburg.',
#     }
#     return render(request, 'backend/base.html', context)