from DjangoParserApp.models import Area, Vacancy
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, ManyToManyField

class Applicant(AbstractUser):
    text = CharField(max_length=32)
    area = ManyToManyField(Area)
    vacancy = ManyToManyField(Vacancy)
