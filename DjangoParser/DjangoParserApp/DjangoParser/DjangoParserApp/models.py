from django.db import models
from django import forms

# Create your models here.
class Skills(models.Model):
    Skill_name = models.CharField(max_length=32, unique=True)

class Vacancy(models.Model):
    Vac_name = models.CharField(max_length=32, unique=True)

class Area(models.Model):
    Area_name = models.CharField(max_length=32, unique=True)

class Request(models.Model):
    Vac_name = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    Area_name = models.ForeignKey(Area, on_delete=models.CASCADE)
    Count_vac = models.IntegerField()
    Up = models.FloatField()
    Down = models.FloatField()
    Skill_name = models.ManyToManyField(Skills)
    Percent = models.FloatField()

class ReqForm(forms.Form):
    vacancy = forms.CharField(label='Вакансия')
    area = forms.CharField(label='Город')







