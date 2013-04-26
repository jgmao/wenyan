from django.db import models

# Create your models here.
class Artical(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField();
    volume = models.CharField(max_length=200,blank=True)
    number = models.IntegerField(default=0);#0 means no number, the number start form 1