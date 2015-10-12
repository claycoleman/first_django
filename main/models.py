from django.db import models

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=255)
    abbrev = models.CharField(max_length=255, null=True, blank=True)   

    class Meta:
        ordering = ['name']
        
    def __unicode__(self):
        return self.name


class StateCapital(models.Model):
    name = models.CharField(max_length=255)
    lat = models.CharField(max_length=255, null=True, blank=True)
    lon = models.CharField(max_length=255, null=True, blank=True)
    population = models.IntegerField(null=True, blank=True)
    # state = models.ForeignKey('State', null=True, blank=True)
    # state = models.ManyToManyField('main.State')
    state = models.OneToOneField('State', null=True, blank=True)

    def __unicode__(self):
        return self.name


class Area(models.Model):
    zip_code = models.CharField(max_length=255, null=True,blank=True)
    lat = models.CharField(max_length=255, null=True, blank=True)
    lon = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    county = models.CharField(max_length=255, null=True, blank=True)
    state_abbrev = models.CharField(max_length=50, null=True, blank=True)
    state = models.ForeignKey('State', null=True, blank=True)

    def __unicode__(self):
        return "%s: %s" % (self.city, self.zip_code)