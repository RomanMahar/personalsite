from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, MultiFieldPanel, \
	InlinePanel, PageChooserPanel, StreamFieldPanel

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel

from wagtail.wagtaildocs.blocks import DocumentChooserBlock

from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import RawHTMLBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock

from modelcluster.fields import ParentalKey
from base.models import CustomImage

class HomePage(Page):
	main_image = models.ForeignKey(
		'wagtailimages.Image',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	heading = models.CharField(
		max_length=50,
		default="Omar Rahman")
	intro = models.CharField(
		max_length=255,
		default="Web Developer, Designer, Illustrator")
	body = RichTextField(blank=True)
	content_panels = Page.content_panels + [
		FieldPanel('body', classname="hero-content"),
		ImageChooserPanel('main_image'),
		FieldPanel('heading'),
		FieldPanel('intro'),
	]
	def get_context(self, request):
		context = super(HomePage, self).get_context(request)
		context['homePageSection'] = HomePageSection.objects.all()
		return context



class LinkFields(models.Model):
	 link_external = models.URLField("External link", blank=True)
	 link_page = models.ForeignKey(
		 'wagtailcore.Page',
		 null=True,
		 blank=True,
		 related_name='+',
		 on_delete=models.SET_NULL,
	 )
	 @property
	 def link(self):
		 if self.link_page:
			 return self.link_page.url
		 else:
			 return self.link_external

	 panels = [
		 PageChooserPanel('link_page'),
	 ]

	 class Meta:
		 abstract = True

class RelatedLink(LinkFields):
	 title = models.CharField(max_length=255, help_text="Link title")
	 main_image = models.ForeignKey(
		 'wagtailimages.Image',
		 null=True,
		 blank=True,
		 on_delete=models.SET_NULL,
		 related_name='+'
	 )
	 description = RichTextField(blank=True)
	 panels = [
		 FieldPanel('title'),
		 ImageChooserPanel('main_image'),
		 MultiFieldPanel(LinkFields.panels, "Link"),
		 FieldPanel('description'),
	 ]

	 class Meta:
		 abstract = True

class HomeProductRelatedLink(Orderable, RelatedLink):
	 page = ParentalKey('home.HomePageSection', related_name='related_links')


class IndexLink(models.Model):
	 link_page = models.ForeignKey(
		 'wagtailcore.Page',
		 null=True,
		 blank=True,
		 related_name='+'
	 )
	 button_text = models.CharField(
		max_length=255, 
		help_text="Button title",
		null=True,
		blank=True,
		default="button"
	)

	 @property
	 def link(self):
		 if self.link_page:
			 return self.link_page.url
		 else:
			 return self.link_external

	 panels = [
		 PageChooserPanel('link_page'),
		 FieldPanel('button_text'),
	 ]
	
class HomePageSection(Page):
	main_image = models.ForeignKey(
		CustomImage,
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	orientation = models.CharField(
		max_length=50, 
		choices= (('left', 'LEFT'), ('right', 'RIGHT'), ('centre', 'CENTRE'), ),
		default='left'
	)
	link_page = models.ForeignKey(
		'wagtailcore.Page',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	button_text = models.CharField(
		max_length=255, 
		help_text="Button title",
		null=True,
		blank=True,
		default="button"
	)
	sectionClassName = models.SlugField(
		max_length=100,
		help_text="no spaces",
		default="homepage-section")
	body = RichTextField(blank=True)
	streamBody = StreamField([
			('heading', blocks.CharBlock(classname="full-title")),
			('paragraph', blocks.RichTextBlock()),
			('image', ImageChooserBlock()),
			('markup', RawHTMLBlock()),
		], null=True, blank=True)

	sectionBackgroundSelector = models.ForeignKey(
		'wagtaildocs.Document',
		null=True,
		blank=True,
		on_delete=models.SET_NULL,
		related_name='+'
	)
	content_panels = Page.content_panels + [
		FieldPanel('orientation'),
		FieldPanel('sectionClassName'),
		MultiFieldPanel(IndexLink.panels, "Related index page"),
		ImageChooserPanel('main_image'),
		DocumentChooserPanel('sectionBackgroundSelector'),
		FieldPanel('body', classname="section-body"),
		StreamFieldPanel('streamBody'),
		InlinePanel('related_links', label="Section link items"),
	]

	def get_context(self, request):
		context = super(HomePageSection, self).get_context(request)
		return context
