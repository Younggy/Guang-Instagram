from django.db import models
from imagekit.models import ProcessedImageField
# Create your models here.
class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to = 'static/image/Posts',
        format = 'JPEG',
        blank = True,
        null = True,)
