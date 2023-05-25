import random

from django.shortcuts import render
from .models import Recipe
from .models import Category


# Create your views here.
def main(request):
    recipes = Recipe.objects.all()
    return render(request, 'main.html', context={'recipes': recipes})


def recipeDetail(request):
    recipe = Recipe.objects.get(title="IngredientsIngredientsIngredients")
    return render(request, 'recipe_detail.html', context={'recipe': recipe})


def categoryList(request):
    categoryList = Category.objects.all()
    return render(request, 'category_list.html', context={'categories': categoryList})

def categoryDetail(request):
    category = Category.objects.get(name="Category1")
    return render(request, 'category_detail.html', context={'category': category})