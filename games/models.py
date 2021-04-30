from django.db import models

# Create your models here.
class Game(models.Model):
    # database fields
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=20)
    price = models.IntegerField()
    files = models.FileField(blank=True, upload_to='files/')

