from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Flag, Solve, User

# Create your views here.


class HomeView(TemplateView):
    template_name = 'backend/base.html'


class SubmitView(TemplateView):
    template_name = 'backend/submit.html'

    def post(self, request):
        flag = request.POST.get('flag')
        user = request.user

        f = Flag.objects.filter(flag=flag).first()
        if f:
            if not f.user.filter(username=user.get_username()):
                message = {
                    'type': 'success',
                    'glyph': 'ok',
                    'text': 'Success!'
                }
                Solve(flag=f, user=user).save()
            else:
                message = {
                    'type': 'info',
                    'glyph': 'repeat',
                    'text': 'Flag already submitted.'
                }
        else:
            message = {
                'type': 'danger',
                'glyph': 'remove',
                'text': 'Flag does not exist!'
            }

        context = {'message': message}
        return render(request, self.template_name, context)
