from django.urls import path, re_path
from django.conf.urls import url
from django.conf.urls.static import static
from mainapp.views import mainapp_index, RecruitGenericCreate, \
    TestDetail, RecruitsList, SithList, \
    RecruitTestResults, recruit_approve, save_test, \
    ReportTotalSithList, ReportSithList

app_name = 'main'

urlpatterns = [
    path('', mainapp_index, name='start_page'),
    path('recruits/create/', RecruitGenericCreate.as_view(), name='recruits_create'),
    re_path('^recruits/test-pass/(?P<slug>\w+)$', TestDetail.as_view(), name='test-pass'),
    re_path('^siths/recruits-list/(?P<slug>\w+)$', RecruitsList.as_view(), name='recruits_list'),
    re_path('^siths/recruit-test-results/(?P<slug>\w+)$', RecruitTestResults.as_view(), name='recruit_test_results'),
    path('siths/', SithList.as_view(), name='sith_list'),
    path('siths/recruit-approve', recruit_approve, name='recruit_approve'),
    path('recruits/save-test/<int:pk>/', save_test, name='save_test'),
    path('reports/total-sith-list', ReportTotalSithList.as_view(), name='report_total_sith_list'),
    path('reports/sith-list', ReportSithList.as_view(), name='report_sith_list'),
]
