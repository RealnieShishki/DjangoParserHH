# Generated by Django 4.1.1 on 2022-09-17 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vac_name', models.CharField(max_length=32, unique=True)),
                ('Area_name', models.CharField(max_length=32, unique=True)),
                ('Skill_name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vac_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjangoParserApp.request')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skill_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjangoParserApp.request')),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjangoParserApp.request')),
            ],
        ),
    ]
