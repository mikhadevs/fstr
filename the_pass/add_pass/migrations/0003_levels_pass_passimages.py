# Generated by Django 5.0 on 2023-12-20 22:19

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('add_pass', '0002_coords_alter_users_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spring', models.CharField(choices=[('1a', '1А'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('3b2', '3Б*')], max_length=3, verbose_name='Весна')),
                ('summer', models.CharField(choices=[('1a', '1А'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('3b2', '3Б*')], max_length=3, verbose_name='Лето')),
                ('autumn', models.CharField(choices=[('1a', '1А'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('3b2', '3Б*')], max_length=3, verbose_name='Осень')),
                ('winter', models.CharField(choices=[('1a', '1А'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('3b2', '3Б*')], max_length=3, verbose_name='Зима')),
            ],
            options={
                'verbose_name': 'Уровень сложности',
                'verbose_name_plural': 'Уровни сложности',
            },
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата добавления')),
                ('status', models.CharField(choices=[('NW', 'новый'), ('PN', 'в обработке'), ('AC', 'принят'), ('RJ', 'отклонён')], default='NW', max_length=2, verbose_name='Статус записи')),
                ('beauty_title', models.CharField(verbose_name='Тип объекта')),
                ('title', models.CharField(verbose_name='Название объекта')),
                ('other_titles', models.CharField(verbose_name='Другое название')),
                ('connect', models.CharField(verbose_name='Подключение')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_pass.levels', verbose_name='Уровень сложности')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_pass.users', verbose_name='Турист')),
            ],
            options={
                'verbose_name': 'Перевал',
                'verbose_name_plural': 'Перевалы',
            },
        ),
        migrations.CreateModel(
            name='PassImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.ImageField(upload_to='images/')),
                ('pass_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='add_pass.pass')),
            ],
        ),
    ]
