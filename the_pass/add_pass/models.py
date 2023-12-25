from django.utils import timezone
from django.db import models


class Users(models.Model):
    email = models.EmailField(max_length=128, unique=True, verbose_name='Электронная почта')
    fam = models.CharField(max_length=40, verbose_name='Фамилия')
    name = models.CharField(max_length=40, verbose_name='Имя')
    otc = models.CharField(max_length=40, blank=True, verbose_name='Отчество')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона с кодом страны')

    class Meta:
        verbose_name = 'Туриста'
        verbose_name_plural = 'Туристы'
    def __str__(self):
        return f'{self.fam}{self.name}{self.otc}'
    



LEVELS = [
    ('1a', '1А'),
    ('1b', '1Б'),
    ('2a', '2А'),
    ('2b', '2Б'),
    ('3a', '3А'),
    ('3b', '3Б'),
    ('3b2', '3Б*'),
]
class Levels(models.Model):
    spring = models.CharField(max_length=3, choices=LEVELS, verbose_name='Весна')
    summer = models.CharField(max_length=3, choices=LEVELS,verbose_name='Лето')
    autumn = models.CharField(max_length=3,choices=LEVELS,verbose_name='Осень')
    winter = models.CharField(max_length=3,choices=LEVELS,verbose_name='Зима')

    class Meta:
        verbose_name = 'Уровень сложности'
        verbose_name_plural = 'Уровни сложности'
    def __str__(self):
        return f'Весна:{self.spring} Лето:{self.summer} Осень:{self.autumn} Зима:{self.winter}'

new = 'NW'
pending = 'PN'
accepted = 'AC'
rejected = 'RJ'

STATUS = [
        (new, "новый"),
        (pending, "в обработке"),
        (accepted, "принят"),
        (rejected, "отклонён"),
    ]
class Pass(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Турист')
    date_added = models.DateTimeField(default=timezone.now, verbose_name='Дата добавления')
    status = models.CharField(max_length=2, choices=STATUS, default='NW', verbose_name='Статус записи')
    level = models.ForeignKey(Levels, on_delete=models.CASCADE, verbose_name='Уровень сложности')
    beauty_title = models.CharField(verbose_name='Тип объекта')
    title = models.CharField(verbose_name='Название объекта')
    other_titles = models.CharField(verbose_name='Другое название')
    connect = models.CharField(verbose_name='Подключение')

    class Meta:
        verbose_name = 'Перевал'
        verbose_name_plural = 'Перевалы'

    def __str__(self):
        return f'{self.pk} {self.beauty_title}{self.status}'


class Coords(models.Model):
    pass_id = models.ForeignKey(Pass, on_delete=models.CASCADE)
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'
    def __str__(self):
        return f'Широта: {self.latitude} Долгота: {self.longitude} Высота: {self.height}'
class PassImages(models.Model):
    pass_id = models.ForeignKey(Pass, on_delete=models.CASCADE, related_name='images')
    image_id = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return f'{self.pk}: {self.pass_id} {self.image_id}'

