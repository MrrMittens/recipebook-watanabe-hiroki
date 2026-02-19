from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Recipe

all_recipes = {
    "recipes": [
        {
            "name": "Recipe 1",
            "ingredients": [
                {
                    "name": "tomato",
                    "quantity": "3pcs"
                },
                {
                    "name": "onion", 
                    "quantity": "1pc"
                },
                {
                    "name": "pork",
                    "quantity": "1kg"
                },
                {
                    "name": "water",
                    "quantity": "1L"
                },
                {
                    "name": "sinigang mix",
                    "quantity": "1 packet"
                }
            ],
            "link": "/recipe/1"
        },
        {
            "name": "Recipe 2",
            "ingredients": [
                {
                    "name": "garlic",
                    "quantity": "1 head"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "vinegar",
                    "quantity": "1/2cup"
                },
                {
                    "name": "water",
                    "quantity": "1 cup"
                },
                {
                    "name": "salt",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "whole black peppers",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "pork",
                    "quantity": "1 kilo"
                }
            ],
            "link": "/recipe/2"
        }
    ]
}

def recipe_list(request):
    ctx = all_recipes
    return render(request, "recipe_list.html", ctx)

def recipe1(request):
    ctx = all_recipes["recipes"][0]
    return render(request, "recipe.html", ctx)

def recipe2(request):
    ctx = all_recipes["recipes"][1]
    return render(request, "recipe.html", ctx)

class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html" 

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe_detail.html" 