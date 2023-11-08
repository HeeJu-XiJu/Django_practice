from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass
# article_set = 장고가 자동으로 추가해주는 컬럼
# comment_set = 장고가 자동으로 추가해주는 컬럼