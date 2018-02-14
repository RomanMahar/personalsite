from __future__ import unicode_literals

from django import forms
from django.db import models
from home.models import LinkFields

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField

from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, MultiFieldPanel, \
    InlinePanel, PageChooserPanel, StreamFieldPanel, BaseFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock

class RecipeItem(LinkFields):
     name_of_ingredient = models.CharField(
     	max_length=255,
     	default="apples",
     	help_text="Ingredient: e.g. 'Flour' ",
     	)
     amount = models.CharField(
     	max_length=255,
     	help_text="Amount: e.g. '1 2/3 cups'",
     	blank=True)
     this_or_next = models.BooleanField(
     	help_text="Adds 'Or' between this and next ingredient",
     	blank=True,
     	default=False,)
     description = RichTextField(blank=True)
     panels = [
         FieldPanel('amount'),
         FieldPanel('name_of_ingredient'),
         FieldPanel('description'),
         FieldPanel('this_or_next'),
     ]
     class Meta:
         abstract = True

class RecipeProfile(Orderable, RecipeItem):
     page = ParentalKey('recipes.Recipe', related_name='ingredient_items')

class Recipe(Page):
	main_image = models.ForeignKey(
	    'wagtailimages.Image',
	    null=True,
	    blank=True,
	    on_delete=models.SET_NULL,
	    related_name='+'
	)
	subrecipe_only = models.BooleanField(
		help_text="Hides recipe from main index view (aka: list view)",
		blank=True,
		default=False,)
	featured_recipe = models.BooleanField(
		help_text="Shows recipe in featured recipe section",
		blank=True,
		default=False,)
	blurb = RichTextField(blank=True, max_length=1200)
	body = RichTextField(blank=True)

	content_panels = Page.content_panels + [
	    # MultiFieldPanel(Ingredient.panels, 'ingredientthings'),
	    MultiFieldPanel([
		    	FieldPanel('subrecipe_only'),
		    	FieldPanel('featured_recipe'),
		    	],
	    	heading="Recipe page options",
	    	classname="collapsible collapsed"
	    	),
	    ImageChooserPanel('main_image'),
	    FieldPanel('blurb'),
	    FieldPanel('body', classname="recipe-body"),
	    InlinePanel('recipe_in_recipe', label='Recipe within recipe'),
	    InlinePanel('ingredient_items', label='ingredients'),
	]
	parent_page_types = ['recipes.RecipeIndex']
	def get_context(self, request):
		context = super(Recipe, self).get_context(request)
		context['Recipe'] = Recipe.objects.all()
		return context

class RecipeInRecipe(models.Model):
	link_external = models.URLField("External link", blank=True)
	heading = models.CharField(
		max_length=255,
		help_text="Heading text for subrecipe (optional)",
		blank=True,
		null=True)
	recipe_in_recipe_page = models.ForeignKey(
    	'Recipe',
    	null=True,
    	blank=True,
    	related_name='+',
    	on_delete=models.SET_NULL,
    )
	panels = [
        PageChooserPanel('recipe_in_recipe_page'),
    ]
	class Meta:
		abstract = True
	def get_context(self, request):
		context = super(RecipeInRecipe, self).get_context(request)
		context['RecipeInRecipe'] = RecipeInRecipe.objects.all()
		return context


class RecipeInRecipeProfile(Orderable, RecipeInRecipe):
    page = ParentalKey(
    	'recipes.Recipe',
    	related_name='recipe_in_recipe',
    	blank=True,
    	null=True,
    	)


class RecipeIndex(Page):
	content_panels = Page.content_panels + [
	    # MultiFieldPanel(Ingredient.panels, 'ingredientthings'),
	]

	def get_context(self, request):
		context = super(RecipeIndex, self).get_context(request)
		context['RecipeIndex'] = Recipe.objects.child_of(self).live()
		return context