from django.core.exceptions import ValidationError
from django.db import models
from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Номер поезда')

    travel_time = models.PositiveSmallIntegerField(verbose_name='Время в пути')

    from_city = models.ForeignKey(City, on_delete=models.CASCADE,
                                  verbose_name='Из какога города')

    to_city = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='to_city_set',
                                verbose_name='В какого город')

    def __str__(self):
        return f"Поезд № {self.name} из города  {self.from_city}"

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Изминит Город прибытия')
        qs = Train.objects.filter(
            from_city=self.from_city,
            to_city=self.to_city,
            travel_time=self.travel_time).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError("Изменити время в пути")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class TrainTest(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Номер поезда')

    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city',
                                  verbose_name='Из какога города')



# from cities.models import City
#
# from trains.models import TrainTest
#
# city = City.objects.first()
#
# >>> tr = TrainTest(name='tr2', from_city=city)
