from django.contrib import admin
from .models import Group, Audience, Category, Training_Format, Course, Payment_info


@admin.register(Group)
class UserAdmin(admin.ModelAdmin):
    list_display = ('number',)
    search_fields = ('number',)


@admin.register(Audience)
class AudienceAdmin(admin.ModelAdmin):
    list_display = ('number', )
    search_fields = ('number',)


@admin.register(Training_Format)
class Training_Format(admin.ModelAdmin):
    list_display = ('is_online', )
    search_fields = ('is_online', )


@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')


@admin.register(Payment_info)
class PaymentInfo(admin.ModelAdmin):
    list_display = ('sec_paid_date', 'sec_paid_amount')
    search_fields = ('sec_paid_date', 'sec_paid_amount')


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
