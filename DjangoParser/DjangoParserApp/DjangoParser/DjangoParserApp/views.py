from django.shortcuts import render
from .models import Request, ReqForm, Skills, Area, Vacancy
from HH_api import vac_request

def main_view(request):
    if request.method == 'POST':
        form = ReqForm(request.post)
        if form.is_valid():
            vacancy = form.cleaned_data['vacancy']
            area = form.cleaned_data['area']
            if Vacancy.objects.filter(vacancy) != vacancy:
                pass
            else:
                Vacancy.objects.create(Vac_name=vacancy)
            if Area.objects.filter(area) != area:
                pass
            else:
                Area.objects.create(Area_name=area)
        else:
            return render(request, 'DjangoParserApp/index.html', context={'form': form})
    else:
        form = ReqForm()
        return render(request, 'DjangoParserApp/index.html', context={'form': form})

def result(request):
    form = ReqForm(request)
    vac = form.cleaned_data['vacancy']
    ar = form.cleaned_data['area']
    vacancy = Vacancy.objects.filter(vac)
    area = Vacancy.objects.filter(ar)
    result = vac_request(vacancy, area)

    return render(request, 'DjangoParserApp/result.html', context={'result': result})

def about(request):
    pass
    return render(request, 'DjangoParserApp/about.html', context={})