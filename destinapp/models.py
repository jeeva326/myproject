from django.db import models

# Create your models here.
class Destin(models.Model):
    PlaceName=models.CharField(max_length=250)
    Weather=models.CharField(max_length=250)
    Location=models.CharField(max_length=500)
    GoogleMap=models.URLField(max_length=800)
    PlaceImage=models.ImageField(upload_to='tourmedia/')
    Description=models.CharField(max_length=1000)