import ast

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib import messages
from django.views.generic import (
    TemplateView,
    FormView, CreateView, UpdateView,
    DeleteView, ListView, DetailView,
)
from django.db import models
from django.db.models import Count
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.shortcuts import redirect
from django.core.mail import send_mail

from mainapp.models import Recruit, Test, Sith, TestResult, Mentoring, Question
from mainapp.forms import RecruitModelForm, TestModelForm, SithForm


def mainapp_index(request):
    return render(request, 'mainapp/index.html', {'message': ''})


# For recruits
# class CategoryGenericCreate(SuperUserMixin, CreateView):
class RecruitGenericCreate(CreateView):
    model = Recruit
    form_class = RecruitModelForm
    template_name = 'create.html'

    # success_url = reverse_lazy('main:start_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вступить в ряды'
        context['OK_text'] = 'Далее'
        return context

    def get_success_url(self):
        return reverse('main:test-pass', kwargs={'slug': self.object.id})


class TestDetail(DetailView):
    model = Recruit
    form_class = TestModelForm
    template_name = 'mainapp/test.html'
    success_url = reverse_lazy('main:start_page')
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recruit = Recruit.objects.get(id=self.kwargs['slug'])
        test = Test.objects.filter(orden=recruit.planet)
        context['test'] = test
        context['recruit'] = recruit
        return context


def save_test(request, pk):
    data = list(ast.literal_eval(request.POST["data"]))
    recruit = Recruit.objects.get(id=int(pk))
    for row in data:
        question = Question.objects.get(id=int(row.get('question')))
        TestResult(recruit=recruit, question=question, answer=row.get('answer')).save()
    success_url = redirect('main:start_page')
    return success_url


# For sith
class SithList(ListView):
    template_name = 'mainapp/sith.html'
    queryset = Sith.objects.order_by('name')
    context_object_name = 'sith'


class RecruitsList(ListView):
    template_name = 'mainapp/recruits_list.html'

    # queryset = Sith.objects.order_by('name')

    def get_queryset(self):
        self.request.session["sith"] = self.kwargs['slug']
        sith = Sith.objects.get(name=self.kwargs['slug'])
        mentor_inactive = Mentoring.objects.filter(is_active=False).exclude(is_refuse=False)
        mentor_active = Mentoring.objects.filter(is_active=True)
        mentor_all = mentor_active | mentor_inactive
        recruit_has_mentor = [i.recruit.id for i in mentor_all]
        qs = TestResult.objects.filter(recruit__planet=sith.planet).distinct('recruit'). \
            exclude(recruit__in=recruit_has_mentor)
        return qs

    context_object_name = 'recruits'


class RecruitTestResults(ListView):
    template_name = 'mainapp/test_results.html'

    def get_queryset(self):
        qs = TestResult.objects.filter(recruit=self.kwargs['slug'])
        return qs

    context_object_name = 'results'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['sith'] = self.request.session["sith"]
        return data


def recruit_approve(request):
    # if request.method == 'POST':
    recruit_id = request.POST['recruit']
    sith_name = request.POST['sith']
    max_students = 3
    # Проверка на кол-во рук тени
    stud_qs = Mentoring.objects.filter(sith__name=sith_name).filter(is_active=True)
    count_students = stud_qs.count()

    if count_students >= max_students:
        students = [st.recruit.name for st in stud_qs]
        students = ', '.join(students)
        message = f'Зачисление невозможно! Максимальное количество Рук тени: {max_students}. Ваши ученики: {students}'
        return render(request, 'mainapp/index.html', {'message': message})

    # Зачислить
    recruit = Recruit.objects.get(id=int(recruit_id))
    sith = Sith.objects.get(name=sith_name)
    new_recruit = Mentoring(recruit=recruit, sith=sith)
    new_recruit.save()
    success_url = redirect('main:recruits_list', slug=sith_name)

    # Отправка письма
    subject = 'Информация о зачислении'
    body = f'{recruit.name}, поздравляем! Вы зачислены в Орден. Ваш наставник: {sith_name}'
    mail_from = settings.EMAIL_HOST_USER
    mail_to = [recruit.email, ]
    send_mail(
        subject,
        body,
        mail_from,
        mail_to,
        fail_silently=False,
    )
    return success_url


# Reports
# Список ситхов с количеством Рук тени
class ReportTotalSithList(ListView):
    template_name = 'mainapp/report_total_sith_list.html'

    def get_queryset(self):
        qs = Mentoring.objects.values('sith__name').annotate(recr_count=Count('recruit'))
        return qs

    context_object_name = 'results'


# Список ситхов, у которых более 1-й руки тени
class ReportSithList(ListView):
    template_name = 'mainapp/report_sith_list.html'

    def get_queryset(self):
        # qs = Mentoring.objects.values('sith__name').annotate(recr_count=Count('recruit'))
        qs = Mentoring.objects.values('sith__name').annotate(recr_count=Count('recruit')).filter(recr_count__gt=1)
        return qs

    context_object_name = 'results'
