from django.db import models


class youtube(models.Model):
    title = models.TextField()
    description = models.TextField()
    thumbnails_URL = models.URLField() 
    channelName = models.TextField()