from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from . managers import UserManager
from django.utils.translation import gettext_lazy as _

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=50,unique=True,verbose_name=_('email'))
    phone_number = models.CharField(max_length=11,unique=True,verbose_name=_('phone_number'))
    full_name = models.CharField(max_length=50,verbose_name=_('full_name'))
    image = models.ImageField(null=True,blank=True,verbose_name=_('image'))
    is_active = models.BooleanField(default=True,verbose_name=_('is_active'))
    is_admin = models.BooleanField(default=False,verbose_name=_('is_admin'))
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS= ['email' , 'full_name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    objects=UserManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

#--------------------------------------------

#create Otp model for send sms and verify user

class OtpCode(models.Model):
    phone_number=models.CharField(max_length=11,unique=True,verbose_name=_('phone_number'))
    code = models.PositiveSmallIntegerField(verbose_name=_('code'))
    created = models.DateTimeField(auto_now_add=True,verbose_name=_('created'))

    class Meta:
        verbose_name = _('OtpCode')
        verbose_name_plural = _('OtpCodes')

    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created}'

#_______________________________________











