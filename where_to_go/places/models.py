from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    summary = models.TextField(blank=True, verbose_name='Краткое описание')
    description = HTMLField(blank=True, verbose_name='Подробное описание')
    longitude = models.FloatField(verbose_name='Долгота')
    latitude = models.FloatField(verbose_name='Широта')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        db_table = 'place'
        
    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(to=Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name='Фото')
    index = models.SmallIntegerField(default=0, db_index=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        db_table = 'place_image'
        ordering = ['index']

    def __str__(self):
        return f'{self.index} {self.place}'
