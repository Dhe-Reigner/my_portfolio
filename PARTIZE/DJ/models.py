from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField('Event Name', max_length=100)
    date = models.DateTimeField('Event date')
    venue = models.CharField('Venue', max_length=100)
    manager = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    