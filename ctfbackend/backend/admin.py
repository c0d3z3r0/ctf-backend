from django.contrib import admin
from .models import Category, Challenge, Flag, Hint, Solve, BuyHint

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    pass


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
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
