from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cuenta
# Register your models here.

class CuentaAdmin(UserAdmin):
    list_display = ('numero', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('numero',)
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Cuenta, CuentaAdmin)
