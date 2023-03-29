from django.db import models
from authentication.models import CustomUser


class Group(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name='номер группы')
    date_start = models.DateField(null=True, verbose_name='дата начала')
    audience = models.ForeignKey('Audience', on_delete=models.PROTECT, null=True, verbose_name="аудитория")
    course = models.ForeignKey('Course', on_delete=models.PROTECT, null=False, verbose_name="курс")
    mentor = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, verbose_name="ментор")

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name_plural = 'группы'
        verbose_name = 'группа'


class GroupUsers(models.Model):
    user = models.ForeignKey(CustomUser, null=False, on_delete=models.PROTECT, verbose_name="студент",
                             default='Иванов')
    group = models.ForeignKey('Group', verbose_name='номер группы', on_delete=models.PROTECT, default=1)

    def __int__(self):
        return self.user

    class Meta:
        verbose_name_plural = 'группа-юзер'
        verbose_name = 'группа-юзер'


class Audience(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name='номер аудитории')
    is_online = models.BooleanField(verbose_name='онлайн', default=False)
    address = models.ForeignKey('Address', on_delete=models.PROTECT, verbose_name="адрес аудитории")

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name_plural = 'аудитории'
        verbose_name = 'аудитория'


class Address(models.Model):
    address_name = models.CharField(max_length=64, verbose_name='адрес')

    def __str__(self):
        return self.address_name

    class Meta:
        verbose_name_plural = 'адреса'
        verbose_name = 'адрес'


class Course(models.Model):
    duration = models.PositiveSmallIntegerField(verbose_name='продолжительность обучения в днях')
    name = models.CharField(max_length=64, verbose_name='название курса', unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='стоимость')
    category = models.ForeignKey('Category', verbose_name='категория', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'курсы'
        verbose_name = 'курсы'


class PaymentInfo(models.Model):
    first_paid_date = models.DateField(null=True, verbose_name='дата 1-ой оплаты')
    first_paid_amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='сумма 1-ой оплаты')
    sec_paid_date = models.DateField(null=True, verbose_name='дата 2-ой оплаты')
    sec_paid_amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='сумма 2-ой оплаты')

    class Meta:
        verbose_name_plural = 'статус оплаты'
        verbose_name = 'статус оплаты'


class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='пользователь', on_delete=models.CASCADE)
    text = models.CharField(max_length=350, verbose_name='отзыв', null=True)
    is_published = models.BooleanField(verbose_name='опубликовано', default=False)

    class Meta:
        verbose_name_plural = 'отзывы'
        verbose_name = 'отзывы'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'категория'
        verbose_name = 'категория'


class Schedule(models.Model):
    day = models.DateTimeField(verbose_name='дата и время занятия', null=False)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, verbose_name="номер группы")

    class Meta:
        verbose_name_plural = 'расписания'
        verbose_name = 'расписание'


class Task(models.Model):
    day = models.ForeignKey('Schedule', on_delete=models.PROTECT, verbose_name="дата и время занятия")
    description = models.CharField(max_length=50, verbose_name='описание задачи', null=False)
    doc = models.CharField(max_length=1024, verbose_name='материалы по задаче', null=False)

    class Meta:
        verbose_name_plural = 'задачи'
        verbose_name = 'задача'
