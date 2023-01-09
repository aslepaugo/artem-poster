from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Location name')
    summary = models.TextField(blank=True, verbose_name='Summary')
    description = HTMLField(blank=True, verbose_name='Description')
    longitude = models.FloatField(verbose_name='Longitude')
    latitude = models.FloatField(verbose_name='Latitude')

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'
        db_table = 'place'
        unique_together = [['title', 'longitude', 'latitude']]
        
    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(to=Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name='Picture')
    index = models.SmallIntegerField(default=0, db_index=True)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        db_table = 'place_image'
        ordering = ['index']

    def __str__(self):
        return f'{self.index} {self.place}'
