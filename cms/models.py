from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=191)
    desc = models.TextField(blank=True, null=True)
    keywords = models.CharField(max_length=191, blank=True, null=True)
    parent = models.ForeignKey("self", blank=True, null=True, db_index=True)

    created_at = models.PositiveIntegerField(null=True, blank=True)
    updated_at = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        pass

    def __unicode__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=191)
    desc = models.TextField(blank=True, null=True)
    keywords = models.CharField(max_length=191, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = HTMLField()
    created_at = models.PositiveIntegerField(null=True, blank=True)
    updated_at = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        pass

    def __unicode__(self):
        return self.title
