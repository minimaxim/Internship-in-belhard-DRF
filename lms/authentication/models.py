

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True, verbose_name="роль пользователя")


class Role(models.Model):
    name = models.CharField(max_length=15, unique=True, verbose_name='роль пользователя', null=True, default='студент')

    class Meta:
        verbose_name_plural = 'роль пользователя'
        verbose_name = 'роль пользователя'

    def __str__(self):
        return self.name