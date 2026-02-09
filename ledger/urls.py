from django.urls import path
from .views import recipe_list, recipe1, recipe2

urlpatterns = [
    path('list', recipe_list, name="recipe_list"),
    path('1', recipe1, name="recipe1"),
    path('2', recipe2, name="recipe2"), 
]

app_name = 'ledger'