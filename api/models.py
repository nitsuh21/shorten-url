from django.db import models

class URLMapping(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
