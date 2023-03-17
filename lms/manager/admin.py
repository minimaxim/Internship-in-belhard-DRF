from django.contrib import admin
from .models import Group, Audience, Category, Course, Role, Schedule


@admin.register(Group)
class UserAdmin(admin.ModelAdmin):
    list_display = ('number',)
    search_fields = ('number',)


@admin.register(Audience)
class AudienceAdmin(admin.ModelAdmin):
    list_display = ('number', )
    search_fields = ('number',)


@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Role)
class Category(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Schedule)
class Category(admin.ModelAdmin):
    list_display = ('days', 'group')


