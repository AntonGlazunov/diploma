# Generated by Django 4.2.16 on 2024-10-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_category_alter_movie_options_remove_movie_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ManyToManyField(to='content.category', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='view_movies',
            field=models.CharField(choices=[('fi', 'Фильм'), ('se', 'Сериал'), ('cs', 'Мультсериал'), ('ca', 'Мультфильм')], max_length=2, verbose_name='Вид контента'),
        ),
    ]
