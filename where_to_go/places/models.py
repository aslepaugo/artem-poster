from django.db import models

class Place(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=400)
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        db_table = 'place'
        
    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(to=Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()
    index = models.SmallIntegerField()

    class Meta:
        db_table = 'place_image'

    def __str__(self):
        return f'{self.index} {self.place}'
