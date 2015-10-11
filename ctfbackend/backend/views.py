from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Flag, Solve, User, Challenge, Category, Hint, BuyHint
from django.db.models import Sum
import math
from .forms import RegistrationForm
from registration.backends.hmac.views import \
    RegistrationView as BaseRegistrationView

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

    def get(self, request):
        scores = User.objects.all()

        for s in scores:
            solves = s.solve_set.aggregate(
                Sum('flag__credits'))['flag__credits__sum'] or 0
            hints = s.buyhint_set.aggregate(
                Sum('hint__price'))['hint__price__sum'] or 0
            s.credits = solves - hints

        context = {'scores': scores}
        return render(request, self.template_name, context)


#class StatisticsView(TemplateView):
#    template_name = 'backend/statistics.html'


class ChallengesView(TemplateView):
    template_name = 'backend/challenges.html'

    def get(self, request, buy_hint=None):
        context = {'open_hint': None}

        if buy_hint:
            hint = Hint.objects.get(pk=buy_hint)
            BuyHint.objects.get_or_create(hint=hint, user=request.user)
            context.update({'open_hint': hint})

        categories = Category.objects.filter(
            challenge__isnull=False,
            challenge__flag__isnull=False
        ).distinct().order_by('name')

        challenges = Challenge.objects.filter(flag__isnull=False).annotate(
            credits=Sum('flag__credits'),
        ).order_by('credits')

        for c in challenges:
            c.progress = math.ceil(
                100 * c.flag_set.filter(user=request.user).count()
                / c.flag_set.count()
            )

        context.update({'challenges': challenges,
                        'categories': categories})
        return render(request, self.template_name, context)


# TODO: just extend User class instead of betterforms?
# Override registration view form
class RegistrationView(BaseRegistrationView):
    form_class = RegistrationForm
