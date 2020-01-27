from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    ''' Custom User Admin '''

    fieldsets = UserAdmin.fieldsets + (
        ('Custom Profile',
         {
            'fields': (
                'avatar',
                'gender',
                'birthdate',
                'language',
                'currency',
                'superhost',)
            },
         ),
    )

#admin.site.register(models.User, CustomUserAdmin)
    # video 26
    # list_display = ('username', 'email', 'gender', 'language', )
    # list_filter = ('language', 'currency','superhost',)
