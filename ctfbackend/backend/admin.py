from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin
from .models import Category, Challenge, Flag, Hint, Solve, BuyHint, Profile, \
    Faculty, Course, File
from django.db.utils import OperationalError
from django.db.models import Case, When, Value, IntegerField
from dynamic_preferences.registries import \
    global_preferences_registry as dynprefs
from dynamic_preferences.models import GlobalPreferenceModel
from dynamic_preferences.admin import \
    GlobalPreferenceAdmin as BaseGlobalPreferenceAdmin
from .dynprefs import order
# Register your models here.

try:
    prefs = dynprefs.manager()
    admin.site.site_header = prefs['general__sitename'] + ' - Administration'
except OperationalError:
    pass


class ChallengeFileInline(SuperInlineModelAdmin, TabularInline):
    model = File
    exclude = ('stage', )
    extra = 0


class StageFileInline(SuperInlineModelAdmin, TabularInline):
    model = File
    exclude = ('challenge', )
    extra = 0


class HintInline(SuperInlineModelAdmin, TabularInline):
    model = Hint
    extra = 0
    ordering = ['order']


class FlagInline(SuperInlineModelAdmin, StackedInline):
    model = Flag
    extra = 0
    ordering = ['stage']
    inlines = [StageFileInline, HintInline]


class ChallengeInline(SuperInlineModelAdmin, StackedInline):
    model = Challenge.categories.through
    extra = 0
    verbose_name = "Challenge"
    verbose_name_plural = "Challenges in this Category"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ChallengeInline]


@admin.register(Challenge)
class ChallengeAdmin(SuperModelAdmin):
    inlines = [ChallengeFileInline, FlagInline]


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    inlines = [StageFileInline, HintInline]


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass


@admin.register(Hint)
class HintAdmin(admin.ModelAdmin):
    pass


@admin.register(Solve)
class SolveAdmin(admin.ModelAdmin):
    pass


@admin.register(BuyHint)
class BuyHintAdmin(admin.ModelAdmin):
    pass


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    pass


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


class ProfileInline(admin.StackedInline):
    model = Profile
    min_num = 1
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Override dynpref admin to apply custom ordering and
# swap name and section column
class GlobalPreferenceAdmin(BaseGlobalPreferenceAdmin):
    list_display = ('verbose_name', 'section', 'name',
                    'help_text', 'raw_value')

    def get_queryset(self, *args, **kwargs):
        # Instanciate default prefs
        dynprefs.manager().all()

        cases = []

        for o in order:
            cases.append(
                When(section=o.section, name=o.name,
                     then=Value(order.index(o)))
            )

        return super(GlobalPreferenceAdmin, self).\
            get_queryset(*args, **kwargs).annotate(
            pref_order=Case(*cases, output_field=IntegerField())
        ).order_by('pref_order')

admin.site.unregister(GlobalPreferenceModel)
admin.site.register(GlobalPreferenceModel, GlobalPreferenceAdmin)
