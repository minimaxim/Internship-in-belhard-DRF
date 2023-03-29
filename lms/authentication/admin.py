from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name",)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'role']
    list_display_links = ['username', 'email']

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'role',
                )
            }
        )
    )
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'role',
                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)






