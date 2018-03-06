from __future__ import unicode_literals

from django.db import models
from wagtail.wagtailimages.models import Image, AbstractImage, AbstractRendition

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, MultiFieldPanel, \
	InlinePanel, PageChooserPanel, StreamFieldPanel

from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel

# Create your models here.

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

class CustomImage(AbstractImage):

	caption = models.CharField(max_length=255, blank=True)
	alt_text = models.CharField(max_length=255, blank=True)
	display_credit = models.BooleanField(
		help_text="redners photographer name as link (if available)",
		blank=True,
		default=False,)
	photographer = models.CharField(max_length=255, blank=True)
	photo_credit_link = models.URLField("External link", blank=True)

	admin_form_fields = Image.admin_form_fields + (
		'caption',
		'alt_text',
		'display_credit',
		'photographer',
		'photo_credit_link'
	)

class CustomRendition(AbstractRendition):
	image = models.ForeignKey('CustomImage', on_delete=models.CASCADE, related_name='renditions')

	class Meta:
		unique_together = (
			('image', 'filter_spec', 'focal_point_key'),
		)
