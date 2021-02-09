from django.db import models


class project(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 250)
    image = models.ImageField(upload_to = 'portfolio/media/')
    url = models.URLField(blank = True)
