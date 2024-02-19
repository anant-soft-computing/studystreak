from django.contrib import admin
from .models import Badge, BadgeDefinition, Category, GamificationInterface, Progression
from .forms import BadgeDefinitionForm

# # Register your models here.
# # django_gamification/admin.py
# from django.contrib import admin
# from .models import Badge, Reward

@admin.register(BadgeDefinition)
class BadgeDefinitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'next_badge','points')
    #fields = ('name', 'description', 'points', 'next_badge')
    form = BadgeDefinitionForm
autocomplete_fields = ['next_badge']
raw_id_fields = ('next_badge',)

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'next_badge','points')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(GamificationInterface)
class GamificationInterfaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'points')

@admin.register(Progression)
class ProgressionAdmin(admin.ModelAdmin):
    list_display = ('progress', 'target')

# @admin.register(Reward)
# class RewardAdmin(admin.ModelAdmin):
#     list_display = ('user', 'points', 'description',)
#     search_fields = ('user__username', 'description',)

