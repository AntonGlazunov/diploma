# Generated by Django 4.2.16 on 2024-10-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_alter_movie_view_movies'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rank',
            field=models.IntegerField(default=0, verbose_name='Важность'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='view_movies',
            field=models.CharField(choices=[('fi', 'Фильм'), ('ca', 'Мультфильм'), ('se', 'Сериал'), ('cs', 'Мультсериал')], max_length=2, verbose_name='Вид контента'),
        ),
    ]
