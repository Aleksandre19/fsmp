from django.db import models
from django.contrib.auth.models import User


# Category model
class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    src = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Subjects model
class Subjects(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    src = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


# Liked videos model
class Likes(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    video = models.ForeignKey('Videos', null=True, blank=True, on_delete=models.SET_NULL)


# My list model
class MyList(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    video = models.ForeignKey('Videos', null=True, blank=True, on_delete=models.SET_NULL)


# Videos model
class Videos(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    subjects = models.ForeignKey('Subjects', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=254)
    content = models.URLField(max_length=1024)
    description = models.TextField()
    watched = models.IntegerField(null=True, blank=True)
    liked = models.IntegerField(null=True, blank=True)
    published = models.DateField(auto_now=False, auto_now_add=True)
    platform = models.CharField(max_length=254, null=True, blank=True)
    my_list_section = models.BooleanField(default=False)
    new_video = models.BooleanField(default=False)
    welcoming = models.BooleanField(default=False)

    def __str__(self):
        return self.title

