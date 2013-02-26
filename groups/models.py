from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    logo_url = models.TextField()
    web_site_url = models.TextField()
    created = models.DateField()
    entity_status = models.SmallIntegerField(default=0)

    def __unicode__(self):
        return self.name
