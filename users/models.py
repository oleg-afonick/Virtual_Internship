from django.db import models


class PassUser(models.Model):
    lastname = models.CharField(max_length=30, verbose_name='Фамилия')
    firstname = models.CharField(max_length=30, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Отчество')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    email = models.EmailField(max_length=150, verbose_name='E-mail')

    class Meta:
        verbose_name = "Турист"
        verbose_name_plural = "Туристы"

    def __str__(self):
        return f"{self.lastname} {self.firstname} {self.surname}"
