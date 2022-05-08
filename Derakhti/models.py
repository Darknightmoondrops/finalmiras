from django.db import models
from Users.models import Users
from extensions.DateJalali import django_jalali

class MainUser(models.Model):
    admin = models.ForeignKey(Users,on_delete=models.CASCADE,default=1,verbose_name='Admin',related_name='mainUser_admin')
    Owner = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name='Owner',related_name='mainUser_owner')
    user = models.ForeignKey(Users,on_delete=models.CASCADE,blank=True,null=True,verbose_name='User')
    identifierـcode = models.CharField(max_length=30,verbose_name='Identifier code')
    places = models.IntegerField(default=1,verbose_name='Places')
    r_or_l = models.BooleanField(default=False,verbose_name='Ruser or Luser')
    payment_status = models.BooleanField(default=False,verbose_name='Payment Status')

    def __str__(self):
        return self.identifierـcode

class Rusers(models.Model):
    main = models.ForeignKey(MainUser,on_delete=models.CASCADE,verbose_name='Main')
    user = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name='User')

    def __str__(self):
        return self.main.identifierـcode


class Lusers(models.Model):
    main = models.ForeignKey(MainUser, on_delete=models.CASCADE, verbose_name='Main')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='User')

    def __str__(self):
        return self.main.identifierـcode



class Contracts(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE,blank=True,null=True,verbose_name='User')
    date = models.DateTimeField(auto_now_add=True,verbose_name='Date')

    def jdate(self):
        return django_jalali(self.date)


    def __str__(self):
        return f'{self.user.id}-{self.user.username}'





class Cards(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE,blank=True,null=True,verbose_name='User')
    first_name = models.CharField(max_length=99,verbose_name='First name')
    last_name = models.CharField(max_length=99,verbose_name='Last name')
    accountـnumber = models.IntegerField(verbose_name='Account number')
    shaba_number = models.IntegerField(verbose_name='Shaba number')
    date = models.DateTimeField(auto_now_add=True,verbose_name='Date')

    def jdate(self):
        return django_jalali(self.date)


    def __str__(self):
        return f'{self.accountـnumber}'