from django.db import models

from core import settings
from images.validators import validate_images_extension


class Image(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    url = models.FileField(upload_to='images/', validators=[validate_images_extension])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
