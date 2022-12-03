from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . forms import UserchangeForm , UserCreationForm
from . models import User , OtpCode


class UserAdmin(BaseUserAdmin):
    form = UserchangeForm
    add_form = UserCreationForm
    list_display = ['email' , 'phone_number' , 'is_admin']
    list_filter = ('is_admin',)
    fieldsets = (
        (None,{'fields':('email','phone_number','full_name','password')}),
        ('permission',{'fields':('is_active','is_admin','last_login')}),
    )

    add_fieldsets = (
        (None,{'fields':('phone_number','email','full_name','password1','password2')}),
    )

    search_fields = ['email','full_name']
    ordering = ('full_name',)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(User,UserAdmin)

@admin.register(OtpCode)
class OtpAdmin(admin.ModelAdmin):
    list_display = ['phone_number','code','created']













