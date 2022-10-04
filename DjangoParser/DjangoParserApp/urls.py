from django.urls import path
from DjangoParserApp import views

app_name = 'DjangoParserApp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('about/', views.about, name='about'),
    path('result/', views.result, name='result')
]
