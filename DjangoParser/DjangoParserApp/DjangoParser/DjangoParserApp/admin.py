from django.contrib import admin
from .models import Request, Vacancy, Area, Skills
# Register your models here.
admin.site.register(Request)
admin.site.register(Vacancy)
admin.site.register(Area)
admin.site.register(Skills)