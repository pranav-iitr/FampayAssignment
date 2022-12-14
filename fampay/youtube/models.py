from django.db import models

# Create your models here.

class youtube(models.Model):
    title = models.TextField()
    description = models.TextField()
    publishing_datetime = models.DateTimeField()
    thumbnails_URLs = models.URLField() 