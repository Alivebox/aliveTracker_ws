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


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    created = models.DateField()
    entity_status = models.SmallIntegerField(default=0)
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    entity_status = models.SmallIntegerField(default=0)

    def __unicode__(self):
        return self.name


class Log(models.Model):
    activity = models.TextField()
    time = models.SmallIntegerField()
    date = models.DateField()
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    group = models.ForeignKey(Group)
    entity_status = models.SmallIntegerField(default=0)

    def __unicode__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=255)
    entity_status = models.SmallIntegerField(default=0)

    def __unicode__(self):
        return self.name


class Permission(models.Model):
    name = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=255)
    entity_status = models.SmallIntegerField(default=0)
    roles = models.ManyToManyField(Role)

    def __unicode__(self):
        return self.name


class Group_User(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    role = models.ForeignKey(Role)

    def __unicode__(self):
        return self.name


class Project_User(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    role = models.ForeignKey(Role)

    def __unicode__(self):
        return self.name


class User_Forgot_Password(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name