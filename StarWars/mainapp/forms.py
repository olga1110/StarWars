from django import forms

from mainapp.models import Recruit, Test, Sith


class RecruitModelForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['name', 'planet', 'age', 'email']


class TestModelForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['question']


class SithForm(forms.ModelForm):
    class Meta:
        model = Sith
        fields = ('name',)
        widgets = {'name': forms.Select()}
        labels = {'name': 'Ваше имя: '}
