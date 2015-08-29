from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Flag, Solve, User
from django.db.models import Sum

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


class ScoreboardView(TemplateView):
    template_name = 'backend/scores.html'

    def chart(self):
        xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
        ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
        chartdata = {'x': xdata, 'y': ydata}
        charttype = "lineChart"
        chartcontainer = 'scoreboard'
        data = {
            'charttype': charttype,
            'chartdata': chartdata,
            'chartcontainer': chartcontainer,
            'extra': {
                'x_is_date': False,
                'x_axis_format': '',
                'tag_script_js': True,
                'jquery_on_ready': False,
            }
        }
        return data

    def get(self, request):
        scores = User.objects.annotate(
            credits=Sum('solve__flag__credits')).order_by('credits').reverse()
        context = {'scores': scores}
        context.update(self.chart())
        return render(request, self.template_name, context)
