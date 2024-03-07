from django.contrib import admin
from .models import alluser,register
# Register your models here.
class AlluserAdmin(admin.ModelAdmin):
    list_display=('email','phone','password','last_login')

class registerAdmin(admin.ModelAdmin):
    list_display=('email','phone','password','user_type','last_login')

admin.site.register(register,registerAdmin)