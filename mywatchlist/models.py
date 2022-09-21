from django.db import models

class WatchAttr(models.Model):
    watched = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()