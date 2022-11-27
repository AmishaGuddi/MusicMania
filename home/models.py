from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length = 200)
    singer = models.CharField(max_length = 200)
    song = models.FileField(upload_to='songs')
    thumbnail = models.FileField(upload_to='thumbnail')

    