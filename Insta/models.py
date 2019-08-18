from django.db import models
from imagekit.models import ProcessedImageField
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    image = ProcessedImageField(
        upload_to = 'static/image/Posts',
        format = 'JPEG',
        blank = True,
        null = True,)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class InstaUser(AbstractUser):
    profile_pic  = ProcessedImageField(
        upload_to = 'static/image/Posts',
        format = 'JPEG',
        blank = True,
        null = True,
    )