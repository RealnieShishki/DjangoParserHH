from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Applicant
from DjangoParserApp.models import Area, Vacancy


class RegForm(UserCreationForm):
    areas = forms.ModelMultipleChoiceField(queryset=Area.objects.all(), widget=forms.CheckboxSelectMultiple())
    vacancy = forms.ModelMultipleChoiceField(queryset=Vacancy.objects.all(), widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Applicant
        fields = ['username', 'password1', 'password2', 'email']