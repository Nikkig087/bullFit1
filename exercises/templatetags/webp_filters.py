from django import template
from cloudinary import CloudinaryImage

register = template.Library()

@register.filter(name='webp')
def convert_to_webp(cloudinary_url, width=None):
    if not cloudinary_url:
        return ""
    
    # Getting the public_id from the Cloudinary URL
    public_id = cloudinary_url.split('/')[-1].split('.')[0]
    
    # Build the WebP URL, applying the width if provided
    if width:
        webp_url = CloudinaryImage(public_id).build_url(format="webp", width=width, crop="scale")
    else:
        webp_url = CloudinaryImage(public_id).build_url(format="webp")
    
    return webp_url
