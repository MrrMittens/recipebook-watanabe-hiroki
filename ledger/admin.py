from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Recipe, RecipeIngredient, Profile


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(admin.BaseUserAdmin):
    inlines = (ProfileInLine,)


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [RecipeIngredientInLine,]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
