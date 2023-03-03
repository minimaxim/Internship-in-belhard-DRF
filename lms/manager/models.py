from django.db import models


class Group(models.Model):
    number = models.SmallIntegerField(default=0, verbose_name='номер группы')
    date_start = models.DateField(blank=True, verbose_name='дата начала')
    audience = models.ForeignKey('Audience', on_delete=models.PROTECT, null=True, verbose_name="аудитория")
    course = models.ForeignKey('Course', on_delete=models.PROTECT, null=True, verbose_name="курс")
    mentor = models.ForeignKey('User', on_delete=models.PROTECT, null=True, verbose_name="ментор")

    class Meta:
        verbose_name_plural = 'группы'
        verbose_name = 'группа'

    def __int__(self):
        return self.number


class User(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')
    email = models.EmailField(max_length=64, unique=True, blank=False, verbose_name='емайл')
    role = models.ForeignKey('Role', on_delete=models.PROTECT, blank=False, verbose_name="роль пользователя")

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'пользователи'
        verbose_name = 'пользователи'


class GroupUsers(models.Model):
    user_id = models.ForeignKey('User', blank=False, on_delete=models.PROTECT, verbose_name="студент",
                                default='Иванов')
    group_id = models.ForeignKey('Group', verbose_name='номер группы', on_delete=models.PROTECT, default=1)

    class Meta:
        verbose_name_plural = 'группа-юзер'
        verbose_name = 'группа-юзер'


class Role(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name='роль пользователя', null=True, default='студент')

    class Meta:
        verbose_name_plural = 'роль пользователя'
        verbose_name = 'роль пользователя'

    def __str__(self):
        return self.name


class Audience(models.Model):
    number = models.SmallIntegerField(default=1, verbose_name='номер аудитории')
    is_online = models.BooleanField(verbose_name='онлайн')
    address = models.ForeignKey('Address', on_delete=models.PROTECT, verbose_name="адрес аудитории")

    def __str__(self):
        return str(self.number)

    def __int__(self):
        return self.number

    class Meta:
        verbose_name_plural = 'аудитории'
        verbose_name = 'аудитория'


class Address(models.Model):
    address_name = models.CharField(max_length=64, verbose_name='адрес')

    def __str__(self):
        return str(self.address_name)

    class Meta:
        verbose_name_plural = 'адреса'
        verbose_name = 'адрес'


class Course(models.Model):
    duration = models.PositiveSmallIntegerField(default=0, verbose_name='продолжительность обучения в днях')
    name = models.CharField(max_length=64, verbose_name='название курса', unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='стоимость')
    category = models.ForeignKey('Category', verbose_name='категория', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'курсы'
        verbose_name = 'курсы'


class PaymentInfo(models.Model):
    first_paid_date = models.DateField(blank=True, verbose_name='дата 1-ой оплаты')
    first_paid_amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='сумма 1-ой оплаты')
    sec_paid_date = models.DateField(blank=True, verbose_name='дата 2-ой оплаты')
    sec_paid_amount = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='сумма 2-ой оплаты')

    class Meta:
        verbose_name_plural = 'статус оплаты'
        verbose_name = 'статус оплаты'


class RolePermission(models.Model):
    role_id = models.ForeignKey('Role', blank=False, on_delete=models.PROTECT, verbose_name="статус пользователя")
    name = models.ForeignKey('Permission', blank=False, on_delete=models.PROTECT, verbose_name="права пользователя")

    class Meta:
        verbose_name_plural = 'роль-разрешение'
        verbose_name = 'роль-разрешение'


class Permission(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='права пользователя ', null=True,
                            default='все права')
    journal = models.BooleanField

    class Meta:
        verbose_name_plural = 'разрешение'
        verbose_name = 'разрешение'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    day = models.DateTimeField(verbose_name='дата и время урока')
    url = models.ForeignKey('LessonMaterial', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'урок'
        verbose_name = 'урок'


class LessonMaterial(models.Model):
    file = models.FileField(upload_to='#', storage=None, max_length=100, )
    name = models.CharField(max_length=64, blank=False, null=True)

    class Meta:
        verbose_name_plural = 'учебные материалы'
        verbose_name = 'учебные материалы'


class Feedback(models.Model):
    user = models.ForeignKey('User', verbose_name='пользователь', on_delete=models.CASCADE, default='0')
    text = models.TextField(max_length=350, verbose_name='отзыв', null=True)

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
