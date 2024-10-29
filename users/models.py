from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import GRAPH
from content.models import NULLABLE, Movie, Category


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    is_block = models.BooleanField(default=False, verbose_name='Заблокирован')
    views = models.ManyToManyField(Movie, verbose_name='просмотры')
    preferences = models.ManyToManyField(Category, verbose_name='предпочтения')


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        permissions = [
            (
                'set_user',
                'Блокировка пользователей'
            )
        ]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
