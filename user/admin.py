from django.contrib import admin
from user.models import Register

# Register your models here.
@admin.register(Register)
class KaamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password1', 'password2']
