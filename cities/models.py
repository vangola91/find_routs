from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name = 'Город')

    def __str__(self):
        return f" name = {self.name}  id  = {self.id}"

    class Meta:

        verbose_name_plural = 'Города'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('cities:detail', kwargs={'pk': self.pk})