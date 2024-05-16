from django.db import models
from django_jalali.db import models as jmodel
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser

from utils.baseModel import BaseModel
from accounts.manager import UserManager


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=12,unique=True,verbose_name='شماره تلفن ')
    first_name = models.CharField(max_length=50,null=True,blank=True,verbose_name='نام')
    last_name = models.CharField(max_length=50,null=True,blank=True,verbose_name='نام خانوادگی')
    postal_code = models.CharField(max_length=10,null=True,blank=True, verbose_name='کد پستی ')
    birthday = models.CharField(max_length=255,null=True,blank=True,verbose_name='تاریخ تولد')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    address = models.TextField(null=True,blank=True,verbose_name='آدرس')
    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name','last_name']

    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_lable):
        return True

    def __str__(self):
        return str(self.phone_number)

    def is_staff(self):
        return self.is_admin


    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        # elif self.first_name:
        #     return self.first_name
        return 'کاربر ناشناس'



class Otp(models.Model):
    code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=

                                    11,null=True)
    created = jmodel.jDateTimeField(auto_now_add=True)