from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    genders = [
        ('mard', 'mard'),
        ('zan', 'zan'),
    ]

    roles = [
        ('derakhti', 'derakhti'),
        ('mlm', 'mlm'),
        ('taksathi', 'taksathi'),
        ('taksathiAdmin', 'taksathiAdmin'),
    ]

    marital = [
        ('motahel', 'motahel'),
        ('mojarad', 'mojarad'),
    ]

    ed = [
        ('diplom', 'diplom'),
        ('lisans', 'lisans'),
    ]
    first_name = models.CharField(max_length=999,verbose_name='First Name')
    last_name = models.CharField(max_length=999,verbose_name='Last Name')
    father_name = models.CharField(max_length=999,verbose_name='Father Name')
    id_passport = models.CharField(max_length=999,verbose_name='Id passport ')
    gender = models.CharField(choices=genders,max_length=999,verbose_name='Gender ')
    role = models.CharField(choices=roles,max_length=50, blank=True,null=True,verbose_name='Rols')
    national_code = models.CharField(unique=True,max_length=999,verbose_name='National Code ')
    mobile1 = models.CharField(max_length=999,verbose_name='Mobile 1')
    marital_status = models.CharField(choices=marital,max_length=999,verbose_name='Marital status')
    education = models.CharField(choices=ed,max_length=999,verbose_name='Education')
    cityـcode = models.CharField(max_length=999,verbose_name='City code')
    phone = models.CharField(max_length=999,verbose_name='Phone')
    mobile2 = models.CharField(max_length=999,verbose_name='Mobile 2')
    dateـofـbirth = models.CharField(max_length=999,verbose_name='Date of birth')
    nationality = models.CharField(max_length=999,verbose_name='Nationality')
    country = models.CharField(max_length=999,verbose_name='Country')
    state = models.CharField(max_length=999,verbose_name='State')
    city = models.CharField(max_length=999,verbose_name='City')
    neighbourhood = models.CharField(max_length=999,verbose_name='Neighbourhood')
    address = models.CharField(max_length=999,verbose_name='Neighbourhood')
    postalـcode = models.CharField(max_length=999,verbose_name='Postal code')
    status = models.BooleanField(default=False,verbose_name='Status')
    Book_or_buy_goods = models.BooleanField(default=False,verbose_name='Book or buy goods')
    identifierـcode = models.CharField(max_length=999,blank=True,null=True,verbose_name='Identifier code')
    walletـbalance = models.IntegerField(default=0,blank=True,null=True,verbose_name='Wallet balance')
    commission = models.IntegerField(default=0,blank=True,null=True,verbose_name='Commission')
    benـkala = models.IntegerField(default=0,blank=True,null=True,verbose_name='Ben Kala')
    REQUIRED_FIELDS = ['first_name', 'last_name','national_code','role']

    def __str__(self):
        return self.first_name