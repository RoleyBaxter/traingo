from django.db import models

# Create your models here.
class HostGroup(models.Model):
    name = models.CharField(max_length = 60, unique = True)
    active = models.BooleanField()
    data_created = models.DateTimeField('date created')
    
    def __unicode__(self):
        return self.name