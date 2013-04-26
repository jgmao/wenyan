from django.db import models

# Create your models here.
class Artical(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField();
    volume = models.CharField(max_length=200,blank=True)
    number = models.IntegerField(default=0)#0 means no number, the number start form 1
    index = models.CharField(max_length=200)
    def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
        self.index = volume+index
        return super(Artical, self).save(force_insert, force_update, using, update_fields)