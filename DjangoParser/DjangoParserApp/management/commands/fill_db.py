from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from DjangoParserApp.models import Request, Skills, Vacancy, VacSkill, Area
import requests
from requests import get
from pycbrf import ExchangeRates
import re
from collections import Counter

class Command(BaseCommand):

    def __init__(self, vacancy, area):
        super().__init__()
        self.vac = vacancy
        self.area = area

    def handle(self, *args, **options):
        res = vac_request(vacancy=self.vac, area=self.area)
        print(res)
        add_Vacancy(res[0])
        add_Area(res[1])
        add_Skills(res[0])
        add_VS(res[0])
        add_Result([0])

def area_req(area):
    DOMAIN = 'http://api.hh.ru/'
    country_url = f'{DOMAIN}areas/'
    if area.islower:
        area = area.capitalize()
    result = requests.get(country_url).json()
    area_id = []
    for i in result:
        areas = i.get('areas')
        for j in areas:
            areas = j.get('areas')
            if j.get('name') == area:
                area_id.append(j.get('id'))
            else:
                for k in areas:
                    if k.get('name') == area:
                        area_id.append(k.get('id'))

    return area_id

def vac_request(vacancy, area):

    DOMAIN = 'http://api.hh.ru/'
    url_vac = f'{DOMAIN}vacancies'
    rate = ExchangeRates()
    area_vac = area_req(area)

    params = {'text': vacancy,
            'area': area_vac}

    r = requests.get(url_vac, params=params).json()

    count_pages = r['pages']
    all_count = len(r['items'])
    result = {'keywords': vacancy,
                'count': all_count}
    skills = []
    sal = {'from': [], 'to': [], 'cur': []}

    for page in range(count_pages):
        param = {'text': vacancy,
                'page': page}
        ress = requests.get(url_vac, params=param).json()
        all_count = len(ress['items'])
        result['count'] += all_count

        for res in ress['items']:
            skill = set()
            res_full = requests.get(res['url']).json()
            pp = res_full['description']
            pp_re = re.findall(r'\n[A-Za-z-?]+', pp)
            its = set(x.strip(' -').lower() for x in pp_re)

            for sk in res_full['key_skills']:
                skills.append(sk['name'].lower())
                skill.add(sk['name'].lower())

            for it in its:
                if not any(it in x for x in skill):
                    skills.append(it)

            if res_full['salary']:
                code = res_full['salary']['currency']
                if rate[code] is None:
                    code = 'RUR'
                k = 1 if code == 'RUR' else float(rate[code].value)
                sal['from'].append(
                    k * res_full['salary']['from'] if res['salary']['from'] else k * res_full['salary']['to'])
                sal['to'].append(
                    k * res_full['salary']['to'] if res['salary']['to'] else k * res_full['salary']['from'])

    sk2 = Counter(skills)
    up = sum(sal['from']) / len(sal['from'])
    down = sum(sal['to']) / len(sal['to'])
    result.update({'down': round(up, 2),
                    'up': round(down, 2)})

    add = []

    for name, count in sk2.most_common(5):
        add.append({'name': name,
                    'count': count,
                    'percent': round((count / result['count']) * 100, 2)})
        result['requirements'] = add
        res = result
    return res, area


def add_Vacancy(res):
    try:
        Vacancy.objects.get(name=res['keywords'])
    except ObjectDoesNotExist:
        Vacancy.objects.create(name=res['keywords'])

def add_Area(area):
    try:
        Area.objects.get(name=area)
    except ObjectDoesNotExist:
        Area.objects.create(name=area)


def add_Skills(res):
    for item in res['requirements']:
        try:
            Skills.objects.get(name=item['name'])
        except ObjectDoesNotExist:
            Skills.objects.create(name=item['name'])


def add_VS(res):
    vac = Vacancy.objects.get(name=res['keywords'])
    for item in res['requirements']:
        skill = Skills.objects.get(name=item['name'])
        r = VacSkill.objects.filter(id_vac=vac, id_skill=skill).first()
        if not r:
            VacSkill.objects.create(id_word=vac, id_skill=skill, count=item['count'], percent=item['percent'])
            print('ws done')
        elif vac.count < res['count']:
            r.count = item['count']
            r.percent = item['percent']
            print('ws edit')
        else:
            print('ws not edit')

def add_Result(res, area):
    try:
        obj = Request.objects.get(Vac_name=res['keywords'], Area_name=area)

        if obj.Vac_name == res['keywords'] and obj.Area_name == area:
            obj.Count_vac = res['count']
            obj.Up = res['up']
            obj.Down = res['down']
            obj.save()
            print('Edit')
        else:
            print('Not edit')
    except ObjectDoesNotExist:
        Request.objects.create(Vac_name=res['keywords'], Count_vac=res['count'], Up=res['up'], Down=res['down'])
