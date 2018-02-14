from django import template

from home.models import HomePageSection

register = template.Library()

@register.inclusion_tag('navbar.html', takes_context=True)
def top_menu(context):
    homepageitems = HomePageSection.objects.all()
    return {
        'homepageitems': homepageitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

