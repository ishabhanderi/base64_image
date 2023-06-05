from django.db import models

class File(models.Model):
  file = models.FileField(blank=False, null=False,upload_to='images/')

class Image(models.Model):
  image = models.ImageField(blank=False, null=False,upload_to='images/')