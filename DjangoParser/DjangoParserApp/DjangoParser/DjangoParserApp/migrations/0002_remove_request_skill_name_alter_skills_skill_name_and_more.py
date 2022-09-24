# Generated by Django 4.1.1 on 2022-09-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoParserApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='Skill_name',
        ),
        migrations.AlterField(
            model_name='skills',
            name='Skill_name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AddField(
            model_name='request',
            name='Skill_name',
            field=models.ManyToManyField(to='DjangoParserApp.skills'),
        ),
    ]
