from django import template

from recipes.models import Recipe, RecipeInRecipe

register = template.Library()

@register.inclusion_tag('recipes.html', takes_context=True)
def recipes_tag(context):
    recipes = Recipe.objects.all()
    return {
        'recipes': recipes,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }



@register.inclusion_tag('recipes.html', takes_context=True)
def recipe_in_recipe_tag(context):
    recipe_in_recipe = RecipeInRecipe.objects.recipe_in_recipe.all()
    return {
        'recipe_in_recipe': recipe_in_recipe,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

