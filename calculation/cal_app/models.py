from django.db import models

# Create your models here.
class Cal(models.Model):
    title = models.CharField(max_length=100)
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    oper = models.CharField(max_length=100)
    output = models.IntegerField()
