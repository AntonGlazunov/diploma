# Generated by Django 4.2.16 on 2024-10-22 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='view_movies',
            field=models.CharField(choices=[('cs', 'Мультсериал'), ('se', 'Сериал'), ('fi', 'Фильм'), ('ca', 'Мультфильм')], max_length=2, verbose_name='Вид контента'),
        ),
    ]
