# Generated by Django 5.0.1 on 2024-02-03 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_for_competitions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competition',
            options={'verbose_name': 'Конкурс', 'verbose_name_plural': 'Конкурсы'},
        ),
        migrations.AlterModelOptions(
            name='competitiontask',
            options={'verbose_name': 'Этап конкурса', 'verbose_name_plural': 'Этапы конкурсов'},
        ),
    ]
