from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    VIEW_MOVIES_CHOICES = {
        ('fi', 'Фильм'),
        ('se', 'Сериал'),
        ('ca', 'Мультфильм'),
        ('cs', 'Мультсериал')
    }
    name = models.CharField(max_length=100, verbose_name='Наименование', unique=True)
    description = models.TextField(verbose_name='Описание')
    view_movies = models.CharField(max_length=2, choices=VIEW_MOVIES_CHOICES, verbose_name='Вид контента')
    category = models.ManyToManyField(Category, verbose_name='Жанр')

    def __str__(self):
        return f'{self.name} {self.view_movies} {self.category}'

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'
