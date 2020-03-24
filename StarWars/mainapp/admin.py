from django.contrib import admin

# Register your models here.

from mainapp.models import Planet, Recruit, Sith, Question, Test, TestResult, Mentoring

admin.site.register(Planet)
# admin.site.register(Recruit)
admin.site.register(Question)
admin.site.register(Test)
# admin.site.register(Sith)
# admin.site.register(TestResult)
admin.site.register(Mentoring)


@admin.register(Recruit)
class RecruitAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'planet_name', 'age', 'email', 'created',
    ]

    list_filter = [
        'name', 'age'
    ]

    search_fields = [
        'name',
    ]

    def planet_name(self, obj):
        return obj.planet.name.title()


@admin.register(Sith)
class SithAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'planet_name', 'created',
    ]

    list_filter = [
        'name',
    ]

    search_fields = [
        'name',
    ]

    def planet_name(self, obj):
        return obj.planet.name.title()


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ['recruit_name', 'question_text', 'answer']

    def recruit_name(self, obj):
        return obj.recruit.name

    def question_text(self, obj):
        return obj.question.text
