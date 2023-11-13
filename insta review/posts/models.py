from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # image = models.ImageField(upload_to='image/%Y/%m')
    image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='image/%Y/%m'
    )