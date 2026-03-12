from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipe_list.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipe_detail.html"
    redirect_field_name = '/accounts/login/'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_add.html'
    login_url = '/accounts/login/'
    success_url = reverse_lazy("ledger:recipe_list")

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'recipe_image.html'
    login_url = '/accounts/login/'

    def get_success_url(self):
        return reverse_lazy(
            'ledger:recipe_detail',
            kwargs={'pk': self.object.recipe.pk}
        )

    def form_valid(self, form):
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    # used to pass recipe to image to get name and pk
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = Recipe.objects.get(pk=self.kwargs['pk'])
        return context
