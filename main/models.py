from django.db import models

# Create your models here.
class Group(models.Model):
        name = models.CharField(max_length=30)
        description = models.TextField()
        logoUrl = models.TextField()
        webSiteUrl = models.TextField()

        def __unicode__(self):
            return self.name