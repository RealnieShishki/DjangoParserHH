from django.contrib import admin
from .models import Request, Vacancy, Area, Skills, VacSkill
# Register your models here.
admin.site.register(Request)
admin.site.register(Vacancy)
admin.site.register(Area)
admin.site.register(Skills)
admin.site.register(VacSkill)