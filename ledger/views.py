from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html"
