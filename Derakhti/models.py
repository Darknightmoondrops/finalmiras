from django.db import models
from Users.models import Users
from extensions.DateJalali import django_jalali
from extensions.optimization import photo_optimization


class MainUser(models.Model):
    admin = models.ForeignKey(Users,on_delete=models.CASCADE,default=1,verbose_name='Admin',related_name='mainUser_admin')
    Owner = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name='Owner',related_name='mainUser_owner')
    user = models.ForeignKey(Users,on_delete=models.CASCADE,blank=True,null=True,verbose_name='User')
    places = models.IntegerField(default=0,blank=True,null=True,verbose_name='Places')
    r_or_l = models.BooleanField(default=False,verbose_name='Ruser or Luser')
    payment_status = models.BooleanField(default=False,verbose_name='Payment Status')




class DepositRequest(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE,blank=True,null=True,verbose_name='User')
    status = models.BooleanField(default=False,verbose_name='Status')
    price = models.IntegerField(verbose_name='Price')
    date = models.DateTimeField(auto_now_add=True,verbose_name='Date')






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




class DerakhtiProductSubCategories_2(models.Model):
    name = models.CharField(max_length=999, verbose_name='Name')

    def __str__(self):
        return f'{self.name}'


class DerakhtiProductSubCategories_1(models.Model):
    name = models.CharField(max_length=999, verbose_name='Name')
    sub_categories2 = models.ManyToManyField(DerakhtiProductSubCategories_2, blank=True, verbose_name='Sub Categories 2')

    def __str__(self):
        return f'{self.name}'


class DerakhtiProductMainCategories(models.Model):
    name = models.CharField(max_length=999, verbose_name='Name')
    image = models.ImageField(upload_to='ProductMainCategoriesImage', blank=True, null=True, verbose_name='Image')
    sub_categories1 = models.ManyToManyField(DerakhtiProductSubCategories_1, blank=True, verbose_name='Sub Categories 1')

    def save(self, *args, **kwargs):
        photo_optimization(self.image)
        super(DerakhtiProductMainCategories, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

class DerakhtiProducts(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE,blank=True,null=True,verbose_name='USer')
    title = models.CharField(max_length=999,verbose_name='Title')
    slug = models.CharField(max_length=999,verbose_name='Slug')
    descriptions = models.CharField(max_length=999,verbose_name='Descriptions')
    image = models.ImageField(upload_to='Products',verbose_name='Image')
    image1 = models.ImageField(upload_to='Products',blank=True,null=True,verbose_name='Image1')
    image2 = models.ImageField(upload_to='Products',blank=True,null=True,verbose_name='Image2')
    image3 = models.ImageField(upload_to='Products',blank=True,null=True,verbose_name='Image3')
    price = models.IntegerField(default=0)
    maincategories = models.ManyToManyField(DerakhtiProductMainCategories,blank=False,verbose_name='Main Category')
    subCategories1 = models.ManyToManyField(DerakhtiProductSubCategories_1,blank=False,verbose_name='Sub Category 1')
    subCategories2 = models.ManyToManyField(DerakhtiProductSubCategories_2,blank=False,verbose_name='Sub Category 2')
    volume = models.CharField(max_length=999,verbose_name='Volume')
    compounds = models.CharField(max_length=999,verbose_name='Compounds')
    licenseـissuer = models.CharField(max_length=999,verbose_name='License issuer')
    date = models.DateTimeField(auto_now_add=True)
    limit = models.IntegerField(default=0,blank=False,null=False,verbose_name='Limit')
    status = models.BooleanField(default=True)
    vocher = models.BooleanField(default=True)

    def jdate(self):
        return django_jalali(self.date)

    def save(self, *args, **kwargs):
        photo_optimization(self.image)
        super(DerakhtiProducts, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class DerakhtiProductsComments(models.Model):
    user = models.ForeignKey(Users,null=False, blank=False,on_delete=models.CASCADE,verbose_name='User')
    product = models.ForeignKey(DerakhtiProducts,null=False, blank=False, on_delete=models.CASCADE,verbose_name='Prodcut Id')
    comment = models.TextField(null=False, blank=False,verbose_name='Comment')
    status = models.BooleanField(default=False, verbose_name='Status')
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Date')

    def user_fullname(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return self.comment





class DerakhtiProductsCarts(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Shoper')
    payment_date = models.DateTimeField(auto_now_add=True,blank=True,null=True, verbose_name='Payment Date')
    payment_status = models.BooleanField(default=False, verbose_name='Payment Status')

    def jdate(self):
        return django_jalali(self.payment_date)

    def __str__(self):
        return f'{self.user}'


class DerakhtiProductsOrders(models.Model):
    cart = models.ForeignKey(DerakhtiProductsCarts, on_delete=models.CASCADE,blank=True,null=True,verbose_name='Cart')
    shopper = models.ForeignKey(Users, on_delete=models.CASCADE,blank=True,null=True,verbose_name='shopper')
    title = models.CharField(blank=True,null=True,max_length=999, verbose_name='Title')
    description = models.TextField(blank=True,null=True,verbose_name='Description')
    price_drsd = models.IntegerField(blank=True, null=True, verbose_name='price_drsd')
    price = models.IntegerField(blank=True, null=True, verbose_name='Price')
    product = models.ForeignKey(DerakhtiProducts,on_delete=models.CASCADE,blank=False, null=False, verbose_name='Product ')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Payment Date')
    payment_status = models.BooleanField(default=False, verbose_name='Payment Status')

    def product_image(self):
        if self.product.image.url:
            return self.product.image.url
        else:
            return None


class CanelProduct(models.Model):
    product = models.ForeignKey(DerakhtiProducts,on_delete=models.CASCADE,verbose_name='Product')
    price = models.IntegerField(default=0,verbose_name='Price')
    user = models.ForeignKey(Users,on_delete=models.CASCADE,verbose_name='User')
    mobile1 = models.CharField(blank=True,null=True,max_length=999,verbose_name='mobile1')
    mobile2 = models.CharField(blank=True,null=True,max_length=999,verbose_name='mobile2')


