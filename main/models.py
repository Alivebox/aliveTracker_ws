from django.db import models

class Group(models.Model):
        name = models.CharField(max_length=30)
        description = models.TextField()
        logo_url = models.TextField()
        web_site_url = models.TextField()
        created = models.DateField()
        entity_status = models.SmallIntegerField(default=0)
        def __unicode__(self):
            return self.name

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    entity_status = models.SmallIntegerField(default=0)
    def __unicode__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    created = models.DateField()
    entity_status = models.SmallIntegerField(default=0)
    def __unicode__(self):
        return self.name