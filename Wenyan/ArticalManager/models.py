from django.db import models

# Create your models here.
class Artical(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField();
    volume = models.CharField(max_length=200,blank=True)
    number = models.IntegerField(default="")#0 means no number, the number start form 1
    index = models.CharField(max_length=200)

    def save(self, force_insert = False, force_update = False, using = None, update_fields = None):
        self.index = self.volume+str(self.number);
        return super(Artical, self).save(force_insert, force_update, using, update_fields)
    @models.permalink
    def get_absolute_url(self):
        return 'show_artical/%' % (self.id)
    def __unicode__(self):
        return self.index

