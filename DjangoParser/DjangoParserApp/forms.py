from django import forms

class ReqForm(forms.Form):
    vacancy = forms.CharField(label='Вакансия')
    area = forms.CharField(label='Город')