from rest_framework import serializers
from .models import *
from django.db.models.fields import TextField

class ContractsSerializers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Contracts
        fields = '__all__'

class CardsSerializers(serializers.ModelSerializer):
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Cards
        fields = '__all__'


class UsersSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    father_name = serializers.CharField(required=False)
    id_passport = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    role = serializers.CharField(required=False)
    national_code = serializers.CharField(required=False)
    mobile1 = serializers.CharField(required=False)
    marital_status = serializers.CharField(required=False)
    education = serializers.CharField(required=False)
    cityـcode = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    mobile2 = serializers.CharField(required=False)
    dateـofـbirth = serializers.CharField(required=False)
    nationality = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    neighbourhood = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    postalـcode = serializers.CharField(required=False)
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Users
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.id_passport = validated_data.get('id_passport', instance.id_passport)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.role = validated_data.get('role', instance.role)
        instance.national_code = validated_data.get('national_code', instance.national_code)
        instance.mobile1 = validated_data.get('mobile1', instance.mobile1)
        instance.marital_status = validated_data.get('marital_status', instance.marital_status)
        instance.education = validated_data.get('education', instance.education)
        instance.cityـcode = validated_data.get('cityـcode', instance.cityـcode)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.mobile2 = validated_data.get('mobile2', instance.mobile2)
        instance.dateـofـbirth = validated_data.get('dateـofـbirth', instance.dateـofـbirth)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.country = validated_data.get('country', instance.country)
        instance.state = validated_data.get('state', instance.state)
        instance.city = validated_data.get('city', instance.city)
        instance.neighbourhood = validated_data.get('neighbourhood', instance.neighbourhood)
        instance.address = validated_data.get('address', instance.address)
        instance.postalـcode = validated_data.get('postalـcode', instance.postalـcode)
        if instance.password == validated_data.get('password'):
            pass
        else:
            instance.set_password(validated_data.get('password'))
        instance.save()
        return instance





class MainUserSerializers(serializers.ModelSerializer):
    user = serializers.CharField(required=False)
    r_or_l = serializers.BooleanField(required=False)
    places = serializers.IntegerField(required=True)
    class Meta:
        model = MainUser
        fields = '__all__'





class DepositRequestSerializers(serializers.ModelSerializer):
    class Meta:
        model = DepositRequest
        fields = '__all__'





class SelectPointsSerializers(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    father_name = serializers.CharField(required=False)
    id_passport = serializers.CharField(required=False)
    gender = serializers.CharField(required=False)
    role = serializers.CharField(required=False)
    national_code = serializers.CharField(required=False)
    mobile1 = serializers.CharField(required=False)
    marital_status = serializers.CharField(required=False)
    education = serializers.CharField(required=False)
    cityـcode = serializers.CharField(required=False)
    phone = serializers.CharField(required=False)
    mobile2 = serializers.CharField(required=False)
    dateـofـbirth = serializers.CharField(required=False)
    nationality = serializers.CharField(required=False)
    country = serializers.CharField(required=False)
    state = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    neighbourhood = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    postalـcode = serializers.CharField(required=False)
    Book_or_buy_goods = serializers.BooleanField(required=True)
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = Users
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.father_name = validated_data.get('father_name', instance.father_name)
        instance.id_passport = validated_data.get('id_passport', instance.id_passport)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.role = validated_data.get('role', instance.role)
        instance.national_code = validated_data.get('national_code', instance.national_code)
        instance.mobile1 = validated_data.get('mobile1', instance.mobile1)
        instance.marital_status = validated_data.get('marital_status', instance.marital_status)
        instance.education = validated_data.get('education', instance.education)
        instance.cityـcode = validated_data.get('cityـcode', instance.cityـcode)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.mobile2 = validated_data.get('mobile2', instance.mobile2)
        instance.dateـofـbirth = validated_data.get('dateـofـbirth', instance.dateـofـbirth)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.country = validated_data.get('country', instance.country)
        instance.state = validated_data.get('state', instance.state)
        instance.city = validated_data.get('city', instance.city)
        instance.neighbourhood = validated_data.get('neighbourhood', instance.neighbourhood)
        instance.address = validated_data.get('address', instance.address)
        instance.postalـcode = validated_data.get('postalـcode', instance.postalـcode)
        instance.Book_or_buy_goods = validated_data.get('Book_or_buy_goods', instance.Book_or_buy_goods)
        if instance.password == validated_data.get('password'):
            pass
        else:
            instance.set_password(validated_data.get('password'))
        instance.save()
        return instance




class UserinfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'



class DerakhtiProductsSerializers(serializers.ModelSerializer):
    price = serializers.IntegerField(required=True)
    vocher = serializers.IntegerField(required=True)
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = DerakhtiProducts
        fields = '__all__'


class DerakhtiProductMainCategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = DerakhtiProductMainCategories
        fields = '__all__'

class DerakhtiProductSubCategories_1Serializers(serializers.ModelSerializer):
    class Meta:
        model = DerakhtiProductSubCategories_1
        fields = '__all__'

class DerakhtiProductSubCategories_2Serializers(serializers.ModelSerializer):
    class Meta:
        model = DerakhtiProductSubCategories_2
        fields = '__all__'




class DerakhtiProductsUpdateSerializers(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    title = serializers.CharField(required=False)
    slug = serializers.CharField(required=False)
    descriptions = TextField(null=True,blank=True)
    image = serializers.ImageField(required=False)
    image1 = serializers.ImageField(required=False)
    image2 = serializers.ImageField(required=False)
    image3 = serializers.ImageField(required=False)
    price = serializers.IntegerField(required=False)
    maincategories = serializers.PrimaryKeyRelatedField(queryset=DerakhtiProductMainCategories.objects.all(), many=True)
    subCategories1 = serializers.PrimaryKeyRelatedField(queryset=DerakhtiProductSubCategories_1.objects.all(), many=True)
    subCategories2 = serializers.PrimaryKeyRelatedField(queryset=DerakhtiProductSubCategories_2.objects.all(), many=True)
    volume = serializers.CharField(required=False)
    compounds = serializers.CharField(required=False)
    licenseـissuer = serializers.CharField(required=False)
    limit = serializers.IntegerField(required=False)
    vocher = serializers.IntegerField(required=False)
    jdate = serializers.ReadOnlyField()

    class Meta:
        model = DerakhtiProducts
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.title = validated_data.get('title', instance.user)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.descriptions = validated_data.get('descriptions', instance.descriptions)
        instance.image = validated_data.get('image', instance.image)
        instance.image1 = validated_data.get('image1', instance.image1)
        instance.image2 = validated_data.get('image2', instance.image2)
        instance.image3 = validated_data.get('image3', instance.image3)
        instance.price = validated_data.get('price', instance.price)
        instance.maincategories.set(validated_data.get('maincategories', instance.maincategories))
        instance.subCategories1.set(validated_data.get('subCategories1', instance.subCategories1))
        instance.subCategories2.set(validated_data.get('subCategories2', instance.subCategories2))
        instance.volume = validated_data.get('volume', instance.volume)
        instance.compounds = validated_data.get('compounds', instance.compounds)
        instance.licenseـissuer = validated_data.get('licenseـissuer', instance.licenseـissuer)
        instance.limit = validated_data.get('limit', instance.limit)
        instance.vocher = validated_data.get('vocher', instance.vocher)
        instance.save()
        return instance


class DerakhtiOrdersSerializers(serializers.ModelSerializer):
    product_image = serializers.ReadOnlyField()
    user_address = serializers.ReadOnlyField()
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = DerakhtiProductsOrders
        fields = '__all__'


class DerakhtiProductsCommentsSerializers(serializers.ModelSerializer):
    user_fullname = serializers.ReadOnlyField()
    jdate = serializers.ReadOnlyField()
    class Meta:
        model = DerakhtiProductsComments
        fields = '__all__'

