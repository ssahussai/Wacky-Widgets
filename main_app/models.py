from django.db import models
from django.urls import reverse

# Create your models here.
class Widget(models.Model):
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.description}'

    def get_absolute_url(self):
        return reverse('home', kwargs={'pk': self.id})