from django.contrib import admin

from .models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('id', 'title')
    #list_filter = ('')
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_per_page = 25

admin.site.register(Gallery, GalleryAdmin)