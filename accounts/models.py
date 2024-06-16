from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser

from .managers import MyUserManager


class MyUser(AbstractBaseUser):
    phone_number =  models.CharField(verbose_name=_('phone number'), max_length=11, unique=True)
    full_name= models.CharField(verbose_name=_('full name'), max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin =models.BooleanField(default=False)

    class Meta:
        verbose_name = _('my users')
        verbose_name_plural = _('my users')


    objects = MyUserManager()

    USERNAME_FIELD ='phone_number'
    REQUIRED_FIELDS =['full_name']
    
    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    @property
    def is_superuser(self):
        return True
    
    
class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11)
    code = models.PositiveSmallIntegerField()
    date_time_created = models.DateTimeField(auto_now_add=timezone.now())

    class Meta:
        verbose_name = _('otp code')
        verbose_name_plural = _('otp code')


    def __str__(self):
        return f'{self.phone_number}:{self.code}'