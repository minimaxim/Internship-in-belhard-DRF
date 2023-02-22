from django.db import models


class Role(models.Model):
    id = models.SmallIntegerField(
        primary_key=True,
        verbose_name='айди'
    )
    name = models.CharField(
        max_length=10,
        unique=True,
        null=False
    )

    class Meta:
        verbose_name = 'роль'
        verbose_name_plural = 'роли'
        db_table = 'roles'


class User(models.Model):
    id = models.BigIntegerField(
        primary_key=True,
        verbose_name='айди'
    )
    first_name = models.CharField(
        max_length=64,
        verbose_name='имя'
    )
    last_name = models.CharField(
        max_length=64,
        verbose_name='фамилия'
    )
    email = models.CharField(
        max_length=64,
        unique=True,
        null=False,
        verbose_name='почта'
    )
    hashed_password = models.CharField(
        max_length=128,
        verbose_name='пароль'
    )
    role_id = models.ForeignKey(
        Role,
        on_delete=models.DO_NOTHING,
        verbose_name='роль'
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        db_table = 'users'


class Permision(models.Model):
    id = models.SmallIntegerField(
        primary_key=True,
        verbose_name='доступ'
    )
    name = models.CharField(
        max_length=128,
        null=False,
        unique=True
    )

    class Meta:
        verbose_name = 'доступ'
        verbose_name_plural = 'доступ'
        db_table = 'доступ'


class Role_permision(models.Model):
    id = models.SmallIntegerField(
        primary_key=True,
        verbose_name='доступ_роли'
    )
    role_id = models.ForeignKey(
        Role,
        on_delete=models.DO_NOTHING,
        verbose_name='роль'
    )
    permision_id = models.ForeignKey(
        Permision,
        on_delete=models.DO_NOTHING,
        verbose_name='доступ'
    )

    class Meta:
        verbose_name = 'доступ_роли'
        verbose_name_plural = 'доступ_роли'
        db_table = 'доступ_роли'