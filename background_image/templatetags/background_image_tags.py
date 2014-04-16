from django import template
from background_image.models import BackgroundImage

register = template.Library()

def background_image_url():
    """ """
    return BackgroundImage.objects.get().img.url

register.simple_tag(background_image_url)