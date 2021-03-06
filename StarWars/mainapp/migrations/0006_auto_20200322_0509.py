# Generated by Django 2.2 on 2020-03-22 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_mentoring_sith_testresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentoring',
            name='is_refuse',
            field=models.BooleanField(default=False, verbose_name='Отказ'),
        ),
        migrations.AlterField(
            model_name='sith',
            name='name',
            field=models.CharField(error_messages={'required': 'Заполните имя!'}, max_length=60, unique=True, verbose_name='Имя'),
        ),
    ]
