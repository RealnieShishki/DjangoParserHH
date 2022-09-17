from django.core.management.base import BaseCommand
from DjangoParserApp.models import Request, Skills

class Command(BaseCommand):

    def handle(self, *args, **options):

        Skills.objects.all().delete()

        Skills.objects.create(Skill_name='python')
        sk = Skills.objects.first()

        Request.objects.create(Vac_name='Python_developer', Area_name='Москва', Count_vac=40,
                               Up=15000.55, Down=345678.34, Skill_name=sk)



