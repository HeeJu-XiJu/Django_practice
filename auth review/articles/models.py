from django.db import models
from accounts.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 1. 권장X
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 2. 권장
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 3. 권장
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)