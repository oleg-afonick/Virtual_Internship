# Generated by Django 4.1.7 on 2023-04-02 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterModelOptions(
            name='level',
            options={'verbose_name': 'Уровень сложности', 'verbose_name_plural': 'Уровни сложности'},
        ),
        migrations.AlterModelOptions(
            name='pereval',
            options={'verbose_name': 'Перевал', 'verbose_name_plural': 'Перевалы'},
        ),
    ]
