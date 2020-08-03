from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='photos/gallery/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    def __int__(self):
        return str(self.id)
