from django.db import models


class Planet(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=60, unique=True,
                            error_messages={'required': 'Укажите наименование планеты'})
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Recruit(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=60,
                            error_messages={'required': 'Заполните имя!'})
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Планета обитания')
    age = models.PositiveIntegerField(verbose_name='Возраст', blank=True)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    def __str__(self):
        return "имя: {}, планета: {}, возраст: {}, email: {}".format(self.name, self.planet, self.age, self.email)

    class Meta:
        ordering = ['name']


class Sith(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=60, unique=True,
                            error_messages={'required': 'Заполните имя!'})
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Планета')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    def __str__(self):
        return "имя: {}, планета: {}".format(self.name, self.planet)

    class Meta:
        ordering = ['name']


class Question(models.Model):
    text = models.TextField(verbose_name='Вопрос',
                            error_messages={'required': 'Заполните текст вопроса!'})


class Test(models.Model):
    orden = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Орден')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')


class TestResult(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, verbose_name='Рекрут')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата ответа")


class Mentoring(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, verbose_name='Рекрут')
    sith = models.ForeignKey(Sith, on_delete=models.CASCADE, verbose_name='Ситх')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата зачисления")
    is_active = models.BooleanField(verbose_name='Запись активна', default=True)
    is_refuse = models.BooleanField(verbose_name='Отказ', default=False)

    class Meta:
        unique_together = ('recruit', 'sith', 'is_active', )





