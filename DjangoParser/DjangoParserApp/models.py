from django.db import models

# Create your models here.
class Skills(models.Model):
    Skill_name = models.CharField(max_length=32, unique=True)

class Request(models.Model):
    Vac_name = models.CharField(max_length=32, unique=True)
    Area_name = models.CharField(max_length=32, unique=True)
    Count_vac = models.IntegerField()
    Up = models.FloatField()
    Down = models.FloatField()
    Skill_name = models.ForeignKey(Skills, on_delete=models.CASCADE)

class Vacancy(models.Model):
    Vac_name = models.ForeignKey(Request, on_delete=models.CASCADE)

class Area(models.Model):
    Area_name = models.ForeignKey(Request, on_delete=models.CASCADE)



