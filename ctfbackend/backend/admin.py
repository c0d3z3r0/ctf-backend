from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin
from .models import Category, Challenge, Flag, Hint, Solve, BuyHint, Profile, Faculty, Course
from dynamic_preferences import global_preferences_registry as dynprefs
# Register your models here.


prefs = dynprefs.manager()
admin.site.site_header = prefs['general__sitename'] + ' - Administration'


class HintInline(SuperInlineModelAdmin, TabularInline):
    model = Hint
    extra = 0
    ordering = ['order']


class FlagInline(SuperInlineModelAdmin, StackedInline):
    model = Flag
    extra = 0
    ordering = ['stage']
    inlines = [HintInline]


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
    inlines = [FlagInline]


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    inlines = [HintInline]


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
