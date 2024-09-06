from django import template
from cloudinary import CloudinaryImage

register = template.Library()

@register.simple_tag
def webp(cloudinary_url, width=250, height=None):
    if not cloudinary_url:
        return ""

    public_id = cloudinary_url.split('/')[-1].split('.')[0]

    transformation = {'format': 'webp', 'width': width, 'crop': 'fit'}
    if height:
        transformation['height'] = height

    webp_url = CloudinaryImage(public_id).build_url(**transformation)
    
    return webp_url