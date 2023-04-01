from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    TYPE_ROLE = (
        ('student', 'студент'),
        ('mentor', 'ментор'),
        ('manager', 'менеджер'),
        ('administrator', 'администратор'),
    )
    name = models.CharField(choices=TYPE_ROLE, max_length=15, unique=True, null=True, verbose_name='роль пользователя',
                            default='student')

    class Meta:
        verbose_name_plural = 'роль пользователя'
        verbose_name = 'роль пользователя'

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True, verbose_name="роль пользователя")
