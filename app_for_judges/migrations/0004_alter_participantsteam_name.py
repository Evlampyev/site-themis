# Generated by Django 5.0.1 on 2024-02-03 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_for_judges', '0003_alter_judge_options_alter_judge_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantsteam',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название команды'),
        ),
    ]
