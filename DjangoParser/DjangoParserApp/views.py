from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Request, ReqForm, VacSkill, Area
from DjangoParserApp.management.commands.fill_db import Command
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin


def main_view(request):
    return render(request, 'DjangoParserApp/index.html')

def result(request):
    if request.method == 'POST':
        form = ReqForm(request.POST)
        if form.is_valid():
            vac = form.cleaned_data['vacancy']
            area = form.cleaned_data['area']
            print(vac, area, sep='\n')
            com = Command(vac, area)
            com.handle()
            res = Request.objects.get(Vac_name=vac, Area_name=area)
            vs = VacSkill.objects.filter(id_word_id=vac.id).all()
            print(res, vs, sep='\n')
            return render(request, 'DjangoParserApp/result.html', context={'res': res, 'vs': vs})
        else:
            form1 = ReqForm
            return render(request, 'DjangoParserApp/index.html', context={'form': form1})
    else:
        form1 = ReqForm
        return render(request, 'DjangoParserApp/index.html', context={'form': form1})

def about(request):

    contacts = [['пр-т Победы д.9 '], ['+7905194524022022'], ['ZOV@vsem.planeta']]

    return render(request, 'DjangoParserApp/about.html', context={'contacts': contacts})


class NameContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        """
        Отвечает за передачу параметров в контекст
        :param args:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'area'
        return context



class areaList(ListView, NameContextMixin):
    model = Area
    template_name = 'DjangoParserHH/about.html'
    context_object_name = 'area'

    def get_queryset(self):
        """
        Получение данных
        :return:
        """
        return Area.objects.all()


class AreaDetailView(DetailView, NameContextMixin):
    model = Area
    template_name = 'DjangoParserHH/about.html'

    def get(self, request, *args, **kwargs):
        """
        Метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.Area_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Получение этого объекта
        :param queryset:
        :return:
        """
        return get_object_or_404(Area, pk=self.Area_id)


class AreaCreateView(CreateView, NameContextMixin):
    fields = '__all__'
    model = Area
    success_url = reverse_lazy('blog:tag_list')
    template_name = 'DjangoParserHH/about.html'

    def post(self, request, *args, **kwargs):
        """
        Пришел пост запрос
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Метод срабатывает после того как форма валидна
        :param form:
        :return:
        """
        return super().form_valid(form)


class AreaUpdateView(UpdateView):
    fields = '__all__'
    model = Area
    success_url = reverse_lazy('blog:tag_list')
    template_name = 'DjangoParserHH/about.html'


class AreaDeleteView(DeleteView):
    template_name = 'DjangoParserHH/about.html'
    model = Area
    success_url = reverse_lazy('blog:tag_list')
