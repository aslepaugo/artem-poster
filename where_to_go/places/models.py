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
