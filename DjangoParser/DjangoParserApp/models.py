from django.db import models


# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Навык')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название навыка'
        verbose_name_plural = 'Навыки'

class Vacancy(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Вакансия')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название вакансии'
        verbose_name_plural = 'Вакансии'

class Area(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название региона'
        verbose_name_plural = 'Регионы'

class Request(models.Model):
    Vac_name = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    Area_name = models.ForeignKey(Area, on_delete=models.CASCADE)
    Count_vac = models.IntegerField()
    Up = models.FloatField()
    Down = models.FloatField()

    def some_method(self):
        return 'hello from method'

    def __str__(self):
        return f'{self.Vac_name}, {self.Area_name}'

class VacSkill(models.Model):
    id_vac = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    id_skill = models.ForeignKey(Skills, on_delete=models.CASCADE)
    count = models.FloatField()
    percent = models.FloatField()








