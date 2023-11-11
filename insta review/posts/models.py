from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image/%Y/%m')
