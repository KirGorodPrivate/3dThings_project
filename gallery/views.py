from django.shortcuts import render

from .models import Gallery

def index(request):
    gallery = Gallery.objects.filter(is_published=True)

    context = {
        'gallery': gallery
    }
    return render(request, 'gallery/gallery.html', context)